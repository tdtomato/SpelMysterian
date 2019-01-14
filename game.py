import deck
import csv

class Play:
    def __init__(self):
        self.__pp = 0
        self.__hand = []
        self.__deck = deck.Deck()
        self.__mysterian_boost = 0
        self.__mysterian_play = 0
        self.__spell_boost = 0
        self.__Anne_played = False
    
    def first_draw(self):
        for i in range(4): #First:3, Second:4 draw
            drawn_card = self.__deck.draw()
            if drawn_card == None:
                break
            self.__hand.append(drawn_card)
        # deck.Deck().recet()
    
    def get_hand(self):
        return sorted(self.__hand, key=lambda c: (c.s_boostable, c.m_boostable, c.cost, not c.draw))
    
    def __draw(self):
        card = self.__deck.draw()
        print('Draw: ' + str(card.name))
        if card is not None and len(self.__hand) < 9:
            self.__hand.append(card)
        else:
            print('燃えました: ' + str(card.name))

    def __play_card(self, play_card):
        print('Play: ' + str(play_card.cost) +'コスト '+play_card.name)
        reduce_cost = 0
        if not play_card.select_draw==None:
            condition = play_card.select_draw
            selected_card = self.__deck.select_draw(condition)
            print('Draw: ' + str(selected_card.name))
            if selected_card is not None and len(self.__hand) < 9:
                self.__hand.append(selected_card)
            else:
                print('燃えました: ' + str(selected_card.name))            

        if play_card.isSpell:
            reduce_cost += 1
            for card in self.__hand:
                self.__spell_boost += card.s_reduce_cost(reduce_cost)

        if play_card.isMysterian:
            self.__mysterian_play += 1
            reduce_cost += 1
            for card in self.__hand:
                self.__mysterian_boost += card.m_reduce_cost(reduce_cost)

        if play_card.addSpell==1:
            if len(self.__hand) < 10:
                self.__hand.append(deck.Common())

        if play_card.draw > 0:
            for i in range(int(play_card.draw)):
                self.__draw()
        
        if play_card.name == 'アン':
            self.__Anne_played = True
    
    def __play(self):
        self.__hand = sorted(self.__hand, key=lambda c: (c.s_boostable, c.m_boostable, not c.draw, c.cost))
        pp_tmp = self.__pp
        for card in self.__hand[:]:
            self.__hand = sorted(self.__hand, key=lambda c: (c.s_boostable, c.m_boostable, c.cost, not c.draw))
            if pp_tmp >= card.cost:
                pp_tmp -= card.cost
                self.__hand.remove(card)
                self.__play_card(card)

    def run_turn(self,writer):
        self.__pp += 1
        if self.__pp == 10:
            writer.writerow([self.__mysterian_play, self.__spell_boost, self.__mysterian_boost, int(self.__Anne_played)])
            return False
        print('Turn' + str(self.__pp))
        self.__draw()
        self.__play()
        return not self.__deck.is_empty()

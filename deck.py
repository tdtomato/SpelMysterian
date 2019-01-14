import random

class Deck:
    def __init__(self):
        cards = \
            [
            Insight(),Insight(),Insight(),
            Knowledge(),Knowledge(),Knowledge(),
            Foresight(),Foresight(),Foresight(),
            Owen(),Owen(),Owen(),
            Missile(),Missile(),Missile(),
            Blast(),Blast(),Blast(),
            Grea(),Grea(),Grea(),
            Tico(),Tico(),Tico(),
            Elenor(),
            Fate(),Fate(),Fate(),
            Miranda(),Miranda(),Miranda(),
            Embrace(),Embrace(),Embrace(),
            Anne(),Anne(),Anne(),
            Zealot(),Zealot(),Zealot()
            ]
        random.shuffle(cards)
        self.__cards = cards

    def recet(self):
        self.__cards.append(Insight())
        random.shuffle(self.__cards)
  
    def draw(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)
    
    def select_draw(self, condition):
        for card in self.__cards:
            cond =  getattr(card, condition)
            if cond:
                return card

    def is_empty(self):
        if len(self.__cards) == 0:
            return True
        return False

class Card:
    def __init__(self, name, cost, draw=0, addSpell=0, isSpell=False, s_boostable=False, m_boostable=False, isMysterian=False, select_draw=None):
        self.name = name
        self.cost = cost
        self.draw = draw
        self.addSpell = addSpell
        self.isSpell = isSpell
        self.s_boostable = s_boostable
        self.m_boostable = m_boostable
        self.isMysterian = isMysterian
        self.select_draw = select_draw

    def s_reduce_cost(self, val):
        if self.s_boostable:
            if not self.name == 'ウインドブラスト':
                self.cost -= val
                if self.cost < 0:
                    self.cost = 0
            return 1
        else:
            return 0

    def m_reduce_cost(self, val):
        if self.m_boostable:
            self.cost -= val
            if self.cost < 0:
                self.cost = 0
            return 1
        else:
            return 0
        

class Insight(Card):
    def __init__(self):
        super().__init__('知恵の光', 1, draw=1, isSpell=True)

class Knowledge(Card):
    def __init__(self):
        super().__init__('マナリアの知識', 1, addSpell=1, isSpell=True)

class Foresight(Card):
    def __init__(self):
        super().__init__('未来視', 2, select_draw='isSpell')

class Owen(Card):
    def __init__(self):
        super().__init__('オーウェン', 2, isMysterian=True, select_draw='isMysterian')

class Missile(Card):
    def __init__(self):
        super().__init__('マジックミサイル', 2, draw=1, isSpell=True)

class Blast(Card):
    def __init__(self):
        super().__init__('ウインドブラスト', 2, s_boostable=True,isSpell=True)

class Grea(Card):
    def __init__(self):
        super().__init__('グレア', 3, isMysterian=True)

class Tico(Card):
    def __init__(self):
        super().__init__('ティコ', 3, addSpell=1, isMysterian=True)

class Elenor(Card):
    def __init__(self):
        super().__init__('エレノア', 3)

class Fate(Card):
    def __init__(self):
        super().__init__('運命の導き', 5, draw=2, s_boostable=True, isSpell=True)

class Miranda(Card):
    def __init__(self):
        super().__init__('ミラ', 6, addSpell=1, m_boostable=True, isMysterian=True)

class Embrace(Card):
    def __init__(self):
        super().__init__('握撃', 8, s_boostable=True, isSpell=True)

class Anne(Card):
    def __init__(self):
        super().__init__('アン', 9, m_boostable=True, isMysterian=True)

class Zealot(Card):
    def __init__(self):
        super().__init__('真実の狂信者', 9, s_boostable=True)

class Common(Card):
    def __init__(self):
        super().__init__('コモンマナリアスペル', 2, isSpell=True, isMysterian=True)

class Sorcery(Card):
    def __init__(self):
        super().__init__('アンの大魔法', 10)
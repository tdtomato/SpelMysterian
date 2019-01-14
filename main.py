from game import *
import csv


filename='result(nerf)_S' + '.csv'


f = open(filename, 'a')
writer = csv.writer(f, lineterminator='\n')

for i in range(10000):
    play = Play()

    play.first_draw()
    while True:
        print("\n[Start Hand]\nCost\tName")
        for card in play.get_hand():
            print(str(card.cost) + card.name)
        if not play.run_turn(writer):
            break

f.close()
import os
import sys
from datetime import date

from game import Game
os.system("clear")

print("\n\n\n\n")

print('FARKLE!!!')
print("##############################################################\n")
print("Farkle as a CLI. What fun!\nCoded by Sir Captain Dr. Professor\n")
print("##############################################################\n\n")

players = []
for i in range(2):
    player = input("Enter player's name: ")
    players.append(player)

print("There are {} players. There names are {}".format(len(players), ", ".join(players)))

game = Game(players=players)
print(game)

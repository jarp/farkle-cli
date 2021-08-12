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

# set some control variables
current_player_index = 0
dice_to_keep = ""

# run while user does not enter x
while True and dice_to_keep != 'x':
    # use the index control variable to get player 1 [0] or 2 [1]
    player = game.players[current_player_index]

    print(f"\n\n\n=================================\n{player} is up!\n=================================\n\n")
    dice_to_keep = input("what dice do you want to keep? ")
import os
import sys
from datetime import date
from models import *
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
standard_dice_count = 6

# run while user does not enter x
while True and dice_to_keep != 'x':
    # use the index control variable to get player 1 [0] or 2 [1]
    player = game.players[current_player_index]

    print(f"\n\n\n=================================\n{player} is up!\n=================================\n\n")
    print("First Role:")

    keeps = [] # the dice to keep
    sets = [] # submitted sets

    for turn in range(10):
        # determine how many dice to role (total - the dice kept by user)
        remaining_dice_count = standard_dice_count - len(keeps)
        print(f'rolling {remaining_dice_count} dice')
        dice_to_keep = input("which do you want to keep? (0  to end turn)  ")

        # control the loop by letting user break out of it
        if dice_to_keep == str(0) or dice_to_keep == 'x':
          message = "OK I guess you are done."

          # ternary Operator to switch player
          current_player_index = 1 if current_player_index == 0 else 0
          break


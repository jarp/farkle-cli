import hashlib
import random

## Main object that is used by the game to control things
class Game:
  def __init__(self, players):
    self.players = players
    self.current_player = None
    self.id = hashlib.md5()
    self.scores = {}
    for player in players:
      self.scores[player] = 0

  def next_player(self):
    print("get next player")
    if self.current_player == None:
      self.current_player = self.players[0]
    else:
      self.current_player = self.players[1] if self.players.index(self.current_player) == 0 else self.players[0]
    print(f"returning {self.current_player}")
    return self.current_player

  def add_points(self, player, points):
    print(f"[add points] adding {points} points for {player}")
    self.scores[player] += points

  def is_over(self):
    for score in self.scores.values():
      if score >= 10000:
        return True
    return False

  def print_scores(self):
    print( "+++++++++++++++++++++++++++++++++++++++++")
    for name in self.scores.keys():
      print(f"++ {name} has {self.scores[name]} points")
    print( "+++++++++++++++++++++++++++++++++++++++++")


## Dice Model that other dice types will inherit from
class Dice:
  def __init__(self):
    print('init')

  def role(self):
    raise "you must implement this method"

## Specific Dice that contains basic sequential numbers
class NumericDice(Dice):
  def __init__(self, number=6):
    self.number = number

  def role(self):
    # print("role a random number bt 1 and ", self.number)
    return random.randint(1, self.number)

## Specific Dice that can be inited with a list of values (ints/strings) Think DnD or Lucky 8 Ball
class ListDice(Dice):
  def __init__(self, values=[]):
    self.values = values

  def role(self):
    random_index = random.randint(0, (len(self.values) -1) )
    # print("get value between 0 and {} which is {}".format( (len(self.values) -1), random_index))
    return self.values[random_index]

## The act of roling 1 or more dice
class Role:
  def __init__(self, number_of_dice=6):
    self.dice = []
    for i in range(number_of_dice):
      self.dice.append(NumericDice())
      self.cup = Cup(dice=self.dice)

  def do(self):
    return self.cup.role()

  @classmethod
  def print_dice(cls, dice):
    print("print all dice", dice)
    d = text2art("".join(map(str, dice)), font='block', chr_ignore=True)
    print(d)

class Cup:
  def __init__(self, dice=[]):
    self.dice = dice

  def role(self):
    results = []
    for die in self.dice:
      results.append(die.role())
    return results
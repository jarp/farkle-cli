import hashlib
import random

class Game:
  def __init__(self, players):
    self.players = players
    self.id = hashlib.md5()
    self.scores = {}
    for player in players:
      self.scores[player] = 0

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

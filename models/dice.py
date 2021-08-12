import random

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

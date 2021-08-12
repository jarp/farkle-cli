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
    dice_as_words = "".join(map(str, dice))
    print(dice_as_words)

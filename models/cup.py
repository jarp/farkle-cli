class Cup:
  def __init__(self, dice=[]):
    self.dice = dice

  def role(self):
    results = []
    for die in self.dice:
      results.append(die.role())
    return results
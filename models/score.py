# 1 	100 points
# 5 	50 points
# Three 1's 	1,000 points
# Three 2's 	200 points
# Three 3's 	300 points
# Three 4's 	400 points
# Three 5's 	500 points
# Three 6's 	600 points
# 1-2-3-4-5-6  	3000 points
# 3 Pairs 	1500 points (including 4-of-a-kind and a pair)

class Score:
  def __init__(self,sets):
    self.sets = []
    for set in sets:
      if len(set) > 0:
        self.sets.append(set)
    self.extract_threes()
    self.clean_up()
    self.total_points = 0
    self.threes_points = { '1': 1000, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600 }


  def points(self):
    if self.total_points > 0:
      return self.total_points

    total_points = 0

    if self.straight():
      total_points = 3000
      self.sets = []
    elif self.three_pair():
      total_points = 1500
      self.sets = []
    if len(self.sets):
      total_points += self.determine_remaining()
    self.total_points = total_points
    return total_points

  def clean_up(self):
    i = 0
    for dice in self.sets:
      if len(dice) == 0:
        self.sets.pop(i)
      i += 1


  def extract_threes(self):
    place_holder_set = []

    for dice in self.sets:
      if len(dice) > 3:
        for s in set(dice):
          if dice.count(s) == 3:
            for i in range(3):
              dice.remove(s)
              place_holder_set.append(s)
    self.sets.append(place_holder_set)
    self.clean_up()

  def determine_remaining(self):
    total_points = 0
    total_points += self.determine_sets_of_three_points()
    total_points += self.orphaned()
    return total_points

  def orphaned(self):
    more_points = 0
    for s in self.sets:
      for i in s:
        if int(i) == 5:
          more_points += 50
        elif int(i) == 1:
          more_points += 100

    return more_points


  def determine_sets_of_three_points(self):
    val = 0
    sets_to_del = []
    print(f"checking sets of 3 for {self.sets}")
    for i in range(len(self.sets)):
      s = self.sets[i]
      print("is it a match? [s,len, lenset]",s, len(s), len(set(s)))
      if len(s) == 3 and len(set(s)) == 1:
        val += self.threes_points[str(s[0])]
        sets_to_del.append(s)

    for i in sets_to_del:
      self.sets.remove(i)
    return val


  def straight(self):
    for s in self.sets:
      if len(set(s)) == 6:
        return True
    return False

  def three_pair(self):
    if len(self.sets) == 3 and  (len(self.sets[0]) == 2 and len(self.sets[1]) == 2):
      return True
    elif len(self.sets) == 2 and (len(self.sets[0]) == 4 or len(self.sets[1]) == 4):
      return True
    return False

  # def pairs(self):
  #   p = self.default_hash()
  #   for s in self.sets:
  #     if len(set(s)) == 1:
  #       p[s[0]] = len(s)

  #   return p

  def max(self):
    return 100000

  def counts(self, set):
    count_hash = {
      '1': self.numbers.count(1),
      '2': self.numbers.count(2),
      '3': self.numbers.count(3),
      '4': self.numbers.count(4),
      '5': self.numbers.count(5),
      '6': self.numbers.count(6)
      }

    return count_hash

  # def default_hash(self):
  #   return {
  #     '1': 0,
  #     '2': 0,
  #     '3': 0,
  #     '4': 0,
  #     '5': 0,
  #     '6': 0
  #     }

  @classmethod
  def is_scorable(cls,dice):
    if 1 in dice:
      return True
    elif 5 in dice:
      return True
    else:
      uniq = set(dice)
      for u in uniq:
        if dice.count(u) == 3:
          return True
    return False

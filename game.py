class Game:
  def __init__(self, players):
    self.players = players
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
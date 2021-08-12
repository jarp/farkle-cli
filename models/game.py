import hashlib

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

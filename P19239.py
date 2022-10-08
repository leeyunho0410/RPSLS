import random
from RPSLS_player import RPSLS_player

class P19239(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    return (random.choice(["rock", "lizard", "paper", "scissors", "spock"]))
  
  def update(self, result: str, competitor_shot: str):
    pass

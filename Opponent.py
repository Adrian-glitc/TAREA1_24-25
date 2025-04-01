from Character import Character
from Player import Player

class Opponent(Character):
    def __init__(self, x, y, image, lives=1):
        super().__init__(x, y, image, lives)

    def collide(self, other):
        if isinstance(other, Player):
            other.gain_score()
            self.is_alive = False
            other.score += 1  # Increment player score when opponent is hit
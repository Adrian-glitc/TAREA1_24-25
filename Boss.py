from Player import Player
from Opponent import Opponent
class Boss(Opponent):
        def __init__(self, x, y, image, lives=5):
            super().__init__(x, y, image, lives)

        def collide(self, other):
            if isinstance(other, Player):
                other.gain_score(5)
                self.lives -= 1
                if self.lives <= 0:
                    self.is_alive = False
                    other.score += 5  # Increment player score when boss is hit
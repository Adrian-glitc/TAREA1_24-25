from Player import Player
from Boss import Boss
class Game:
        def __init__(self):
            self.player = Player(0, 0, "player_image")
            self.opponents = []
            self.boss = None
            self.score = 0

        def remove_opponent(self, opponent):
            if opponent in self.opponents:
                self.opponents.remove(opponent)
            if not self.boss:
                self.boss = Boss(100, 100, "boss_image")

        def end_game(self):
            if self.player.lives <= 0:
                print("Game Over")
            elif self.boss and not self.boss.is_alive:
                print("Victory! You defeated the boss!")

        def display_status(self):
            print(f"Score: {self.player.score} | Lives: {self.player.lives}")

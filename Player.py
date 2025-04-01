from Character import Character
class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0

    def move(self, dx, dy):
        super().move(dx, dy)

    def shoot(self):
        # Placeholder for player shooting logic
        pass

    def gain_score(self, points=1):
        self.score += points
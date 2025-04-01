from Entity import Entity
class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives

    def move(self, dx, dy):
        super().move(dx, dy)

    def shoot(self):
        # Placeholder for shooting logic
        pass

    def collide(self, other):
        # Placeholder for collision logic
        pass

    
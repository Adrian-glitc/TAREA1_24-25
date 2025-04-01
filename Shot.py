from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image)
        self.speed = speed

    def move(self):
        pass

    def hit_target(self, target):
        pass
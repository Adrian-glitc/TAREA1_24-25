class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        # Placeholder for drawing logic
        pass
    
    def collide(self, other):
        # Placeholder for collision logic
        pass
    def is_alive(self):
        return self.lives > 0
    def get_position(self):
        return self.x, self.y
    def get_image(self):
        return self.image
    def get_lives(self):
        return self.lives
    def set_lives(self, lives):
        self.lives = lives
    def set_position(self, x, y):
        self.x = x
        self.y = y
    def set_image(self, image):
        self.image = image
    def __str__(self):
        return f"Entity at ({self.x}, {self.y}) with image {self.image}"
    
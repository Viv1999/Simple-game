class Projectile(object):
    def __init__(self, x, y, radius, color, facing, player):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.player = player

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

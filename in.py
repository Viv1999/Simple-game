import pygame
pygame.init()

# import psyco
#  psyco.full()

win = pygame.display.set_mode((500, 500))
screen_width = 500
screen_height = 480
pygame.display.set_caption('My First game')

clock = pygame.time.Clock()


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0

    def draw(self, win):
        win.blit(bg, (0, 0))

        if self.walk_count + 4 > 27:
            self.walk_count = 0

        if self.left:
            win.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif man.right:
            win.blit(walkRight[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(char, (self.x, self.y))
            self.walk_count = 0


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redraw_game_window():
    man.draw(win)
    pygame.display.update()


man = Player(300, 410, 64, 64)

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width:
        man.x += man.vel
        man.right = True
        man.left = False

    else:
        man.right = False
        man.left = False
        man.walk_count = 0

    if not man.is_jump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        #
        # if keys[pygame.K_DOWN] and y < screen_height - height:
        #     y += vel

        if keys[pygame.K_SPACE]:
            man.is_jump = True
            man.left = False
            man.right = False
            man.walk_count = 0

    else:
        if man.jump_count >= -10:
            if man.jump_count > 0:
                man.y -= (man.jump_count ** 2) * 0.5
            else:
                man.y += (man.jump_count ** 2) * 0.5
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10

    redraw_game_window()

pygame.quit()
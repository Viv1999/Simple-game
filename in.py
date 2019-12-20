import pygame
pygame.init()


win = pygame.display.set_mode((500, 480))
screen_width = 500
screen_height = 480
pygame.display.set_caption('My First game')

clock = pygame.time.Clock()

bullet_sound = pygame.mixer.Sound('bullet.wav')
hit_sound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


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
        self.jump_count = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

        self.score = 0

    def draw(self, win):
        win.blit(bg, (0, 0))

        if self.walk_count + 4 > 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif man.right:
                win.blit(walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            # win.blit(char, (self.x, self.y))
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
            self.walk_count = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


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


class Enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (50/10)*(10 - self.health), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0

    def hit(self, player):
        print('hit')
        hit_sound.play()
        player.score += 1
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redraw_game_window():
    man.draw(win)
    goblin.draw(win)
    text = font.render('Score: ' + str(man.score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []
run = True
shoot_loop = 0
while run:
    clock.tick(27)

    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit(bullet.player)
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        bullet_sound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(man.x + man.width//2, round(man.y + man.height//2), 6, (0, 0, 0), facing, man))
        shoot_loop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walk_count = 0

    if not man.is_jump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        #
        # if keys[pygame.K_DOWN] and y < screen_height - height:
        #     y += vel

        if keys[pygame.K_UP]:
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
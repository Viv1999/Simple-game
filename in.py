import pygame
pygame.init()

# import psyco
#  psyco.full()

win = pygame.display.set_mode((500, 500))
screen_width = 500
screen_height = 480
pygame.display.set_caption('My First game')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64

vel = 5
is_jump = False
jump_count = 10

left = False
right = False
walk_count = 0

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def redraw_game_window():
    global walk_count

    win.blit(bg, (0, 0))

    if walk_count + 4 > 27:
        walk_count = 0

    if left:
        win.blit(walkLeft[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walkRight[walk_count//3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x, y))
        walk_count = 0

    pygame.display.update()


run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
        right = True
        left = False

    else:
        right = False
        left = False
        walk_count = 0

    if not is_jump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        #
        # if keys[pygame.K_DOWN] and y < screen_height - height:
        #     y += vel

        if keys[pygame.K_SPACE]:
            is_jump = True
            left = False
            right = False
            walk_count = 0

    else:
        if jump_count >= -10:
            if jump_count > 0:
                y -= (jump_count ** 2) * 0.5
            else:
                y += (jump_count ** 2) * 0.5
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    redraw_game_window()

pygame.quit()
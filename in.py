import pygame
pygame.init()

# import psyco
#  psyco.full()

win = pygame.display.set_mode((500, 500))
screen_width = 500
screen_height = 500
pygame.display.set_caption('My First game')

x = 50
y = 350
width = 40
height = 60

vel = 5
is_jump = False
jump_count = 10

run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel

    if not is_jump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < screen_height - height:
            y += vel

        if keys[pygame.K_SPACE]:
            is_jump = True

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

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
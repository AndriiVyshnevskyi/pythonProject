import pygame

MAX_X = 571  # Оновлений розмір вікна по осі X
MAX_Y = 1280  # Оновлений розмір вікна по осі Y
game_over = False
bg_color = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("Free Ukraine")

myimage = pygame.image.load("1.png").convert()
myimage = pygame.transform.scale(myimage, (MAX_X, MAX_Y))

x = 0  # Початкова позиція X
y = 0  # Початкова позиція Y

move_right = False
move_left = False
move_up = False
move_down = False

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left:
        x -= 2
        if x < 0:
            x = 0

    if move_right:
        x += 2
        if x > MAX_X - MAX_X:
            x = MAX_X - MAX_X

    if move_up:
        y -= 2
        if y < 0:
            y = 0

    if move_down:
        y += 2
        if y > MAX_Y - MAX_Y:
            y = MAX_Y - MAX_Y

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()

pygame.quit()

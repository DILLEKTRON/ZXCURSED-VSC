import pygame as pg
import random
import sys

pg.init()

W = 1200
H = 900
game_over = False
screen = pg.display.set_mode((W, H))
pg.display.set_caption("cursedbird")
COLOR_GREEN = (0, 255, 0)
COLOR_BLACK = (0, 0, 0)
random_y = random.randint(100, H - 100)
PIPE = pg.Rect(W + 100 , random_y + 100 ,75,H)
PIPE2 = pg.Rect(W + 100 , random_y - 100 - H ,75,H)
pipes = [{'x': 600, 'y': random.randint(-300, -150)}]

BACKGROUND = pg.image.load('fon2.jpg')
BIRD = pg.image.load('cursed.png')
BIRD.convert()
BACKGROUND.convert()

BIRD = pg.transform.scale(BIRD,(78,78))
player = BIRD.get_rect()

speed = 0
accel = 9.8 / 60

player.x = W / 4
player.y = H / 2 - 100

clock = pg.time.Clock()  #

angle = 0

random_y = random.randint(100, H - 100)
pipe1 = pg.Rect(W + 100 , random_y + 100 ,75,H)
pipe2 = pg.Rect(W + 100 , random_y - 100 - H ,75,H)

pipe_speed = 3

while not game_over:
    screen.fill(COLOR_BLACK)
    for event in pg.event.get():
        # print(event)
        if event.type == pg.KEYDOWN and event.key == 27 or event.type == pg.QUIT:
            game_over = True
        if (event.type == pg.KEYDOWN and event.key == 32) or (
            event.type == pg.MOUSEBUTTONDOWN and event.button == 1
        ):
            speed = -5

    if player.top >= H:
        game_over = True


    player.y += speed
    speed += accel

    if player.top < 0:
        player.y = 0
        speed = accel

    angle = -speed * 6
    player_rotated = pg.transform.rotate(BIRD, angle)
    screen.blit(player_rotated, (player.x, player.y))


    pipe1.x += - pipe_speed
    pipe2.x += - pipe_speed

    if pipe1.right < 0:
        pipe1.x = W + 100    
        pipe2.x = W + 100
        random_y = random.randint(100, H - 100)
        pipe1 = pg.Rect(W + 100 , random_y + 100 ,75,H)
        pipe2 = pg.Rect(W + 100 , random_y - 100 - H ,75,H)
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(BIRD, (player.x, player.y))
    pg.draw.rect(screen, COLOR_GREEN, pipe1)
    pg.draw.rect(screen, COLOR_GREEN, pipe2)
    pg.display.update()
    clock.tick(60)









import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

smiley = pygame.image.load("cursed.png")
smiley = pygame.transform.scale(smiley, (smiley.get_width(), smiley.get_height()))

x, y = 0, screen_height // 2 - smiley.get_height() // 2
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    screen.blit(smiley, (x, y))

    x += speed

    if x > screen_width:
        x = -smiley.get_width()

    pygame.display.update()

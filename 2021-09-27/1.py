import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.rect(screen, (152, 152, 152), [0, 0, 1366, 768])
circle(screen, (239, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, width=2)
circle(screen, (255, 0, 0), (155, 155), 25)
circle(screen, (255, 0, 0), (245, 155), 20)
circle(screen, (0, 0, 0), (155, 155), 25, width=2)
circle(screen, (0, 0, 0), (245, 155), 20, width=2)
circle(screen, (0, 0, 0), (155, 155), 12)
circle(screen, (0, 0, 0), (245, 155), 10)
rect(screen, (0, 0, 0), (155, 225, 93, 20))
line(screen, (0, 0, 0), (90, 90), (180, 135), 10)
line(screen, (0, 0, 0), (300, 90), (0.95 * 230, 145), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

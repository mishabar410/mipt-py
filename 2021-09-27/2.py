import pygame
from pygame.draw import *

# горы (179, 179, 179)
# земля (170, 222, 135)
# белый (255, 255, 255)
# небо (175, 221, 233)
# лиловые глаза (229, 128, 255)
# зеленый куст (113, 200, 55)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((397, 562))

# небо, земля и горы

pygame.draw.rect(screen, (175, 221, 233), [0, 0, 397, 562])
polygon(screen, (179, 179, 179), [(0, 562), (397, 562), (397, 50),
                                  (300, 140), (200, 25), (120, 100), (80, 120), (40, 10), (0, 130)])
polygon(screen, (0, 0, 0), [(0, 562), (397, 562), (397, 50), (300, 140),
                            (200, 25), (120, 100), (80, 120), (40, 10), (0, 130)], width=1)
polygon(screen, (170, 222, 135), [(0, 562), (397, 562), (397, 280),
                                  (200, 280), (190, 275), (180, 240), (40, 240), (20, 250), (0, 263)])
polygon(screen, (0, 0, 0), [(0, 562), (397, 562), (397, 280),
                            (200, 280), (190, 275), (180, 240), (40, 240), (20, 250), (0, 263)], width=1)


def draw_cvetochek(x, y, scale):
	l = 15 * scale  # характерный размер цветочка
	x_list = [-0.9  ,  0   , 0.8]
	y_list = [-0.3, -0.5, -0.3]
	for i in range(3):
		ellipse(screen, (255, 255, 255), (x + x_list[i] * l, y + y_list[i] * l, 2 * l, l))
		ellipse(screen, (179, 179, 179), (x + x_list[i] * l, y + y_list[i] * l, 2 * l, l), width=1)
	ellipse(screen, (255, 233, 0), (x, y, 2 * l, l))
	for i in range(3):
		ellipse(screen, (255, 255, 255), (x - x_list[i] * l, y - y_list[i] * l, 2 * l, l))
		ellipse(screen, (179, 179, 179), (x - x_list[i] * l, y - y_list[i] * l, 2 * l, l), width=1)


def draw_klumba(x, y, scale):
	elipse(x, y, scale)

draw_cvetochek(40, 40, 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

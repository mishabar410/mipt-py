import pygame
from pygame.draw import *

# горы (179, 179, 179)
# земля (170, 222, 135)
# белый (255, 255, 255)
# небо (175, 221, 233)
# лиловые глаза (229, 128, 255)
# зеленый куст (113, 200, 55)

# below the colors of objects are declared

mountain_color = (179, 179, 179)
ground_color = (170, 222, 135)
animal_color = (255, 255, 255)
flower_petal_color = (255, 255, 255)
flower_border_color = (179, 179, 179)
sky_color = (175, 221, 233)
eyes_color =  (229, 128, 255)
plant_color = (113, 200, 55)
blik_color = (255, 255, 255)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((397, 562))

# небо, земля и горы

pygame.draw.rect(screen, sky_color, [0, 0, 397, 562])
polygon(screen, mountain_color, [(0, 562), (397, 562), (397, 50),
                                  (300, 140), (200, 25), (120, 100), (80, 120), (40, 10), (0, 130)])
polygon(screen, (0, 0, 0), [(0, 562), (397, 562), (397, 50), (300, 140),
                            (200, 25), (120, 100), (80, 120), (40, 10), (0, 130)], width=1)
polygon(screen, ground_color, [(0, 562), (397, 562), (397, 280),
                                  (200, 280), (190, 275), (180, 240), (40, 240), (20, 250), (0, 263)])
polygon(screen, (0, 0, 0), [(0, 562), (397, 562), (397, 280),
                            (200, 280), (190, 275), (180, 240), (40, 240), (20, 250), (0, 263)], width=1)

# Функция рисует цветочек. А Бориса Хрен Попадешь так зовут, потому что в него хрен попадешь

def draw_cvetochek(x, y, scale, surf):

    # x, y is the object position
    # scale is the object size
    # surf is the surface the flower is to be drawn on

    l = 15 * scale  # l is the charachteristic size of the flower
    x_list = [-0.9, 0, 0.8]
    y_list = [-0.3, -0.5, -0.3]
    for i in range(3):
        ellipse(surf, flower_petal_color,
                (x + x_list[i] * l, y + y_list[i] * l, 2 * l, l))
        ellipse(surf, flower_border_color,
                (x + x_list[i] * l, y + y_list[i] * l, 2 * l, l), width=1)
    ellipse(surf, (255, 233, 0), (x, y, 2 * l, l))
    for i in range(3):
        ellipse(surf, flower_petal_color,
                (x - x_list[i] * l, y - y_list[i] * l, 2 * l, l))
        ellipse(surf, flower_border_color,
                (x - x_list[i] * l, y - y_list[i] * l, 2 * l, l), width=1)

# should_be_flipped bool indicates if big floppa should flop the klumba 

def draw_klumba(x, y, scale, should_be_flipped):

    # x, y is the object position
    # scale is the object size
    # should_be_flipped indicates whether the object is to be flipped horizontally

	klumba_surf = pygame.Surface((scale * 70, scale * 70), pygame.SRCALPHA, 32)
	klumba_surf = klumba_surf.convert_alpha()
    # pygame.draw.rect(klumba_surf, (170, 222, 135), [0, 0, 397, 562])
	circle(klumba_surf, plant_color, (scale * 35, scale * 35), scale * 35)
	for i in [(12, 18), (30, 8), (45, 18), (31, 31), (12, 31), (20, 45), (40, 50), (45, 35)]:
	    draw_cvetochek(scale * i[0], scale * i[1], scale * 0.5, klumba_surf)
	if(should_be_flipped == True):
	    klumba_surf = pygame.transform.flip(klumba_surf, True, False)
	screen.blit(klumba_surf, (x, y))

#Рисует жвотне ногу

def draw_animal_leg(x, y, scale, surface):

    # x, y is the object position
    # scale is the object size
    # surf is the surface the flower is to be drawn on

	leg_surf = pygame.Surface((scale*35, scale*100), pygame.SRCALPHA, 32)
	leg_surf = leg_surf.convert_alpha()
	ellipse(leg_surf, animal_color, (0, 0, scale*25, scale*40))
	ellipse(leg_surf, animal_color, (0, scale*40, scale*25, scale*40))
	ellipse(leg_surf, animal_color, (0, scale*80, scale*35, scale*20))
	surface.blit(leg_surf, (x, y))

# Функция рисует жвотне ухи

def draw_animal_ear(x, y, scale, surface):

    # x, y is the object position
    # scale is the object size
    # surf is the surface the flower is to be drawn on

	polygon(surface, animal_color, [(x, y), (x + scale*10, y+ scale*3), (x+scale*4, y - scale*3)])

# Функция рисует жвотню

def draw_animal(x, y, scale, should_be_flipped):

    # x, y is the object position
    # scale is the object size
    # should_be_flipped indicates whether the object is to be flipped horizontally

    ani_surf = pygame.Surface((scale*250, scale*300), pygame.SRCALPHA, 32)
    ani_surf = ani_surf.convert_alpha()
    ellipse(ani_surf, animal_color, (scale*30, scale*100, scale*200, scale*60)) #draws the main body
    ellipse(ani_surf, animal_color, (scale*200, 0, scale*30, scale*140)) #draws the neck
    ellipse(ani_surf, animal_color, (scale*190, 0, scale*60, scale*40)) #draws the head
    draw_animal_ear(179*scale, 10*scale, scale*3, ani_surf)
    draw_animal_ear(178*scale, 20*scale, scale*3, ani_surf)
    for i in [(40*scale,120*scale), (80*scale,140*scale), (120*scale,125*scale), (160*scale, 140*scale)]:
        draw_animal_leg(i[0], i[1], scale, ani_surf)
    circle(ani_surf, eyes_color, (230*scale, 15*scale), 12*scale)
    circle(ani_surf, (0, 0, 0), (235*scale, 15*scale), 8*scale)
    blik_surf = pygame.Surface((scale*10, scale*5), pygame.SRCALPHA, 32)
    blik_surf = blik_surf.convert_alpha()
    ellipse(blik_surf, blik_color, (0, 0, scale*10, scale*5))
    blik_surf = pygame.transform.rotate(blik_surf, -60)
    ani_surf.blit(blik_surf, (225*scale, 5*scale))
    if(should_be_flipped == True):
        ani_surf = pygame.transform.flip(ani_surf, True, False)	
    screen.blit(ani_surf, (x, y))


draw_klumba(200, 390, 2, True)
# draw_animal(-150, 290, 2, False)
draw_klumba(10, 250, 1, False)
draw_animal(-290, 150, 2, False)
draw_animal(240, 180, 0.5, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

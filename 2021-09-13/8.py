# во сем (спирал квадратб)

import turtle
turtle.shape('turtle')
turtle.speed('fastest')


def spiral(a, dphi):
    for i in range(1, 30, 1):
        turtle.forward(a * dphi * (1 + (i * dphi)**2)**0.5)
        turtle.left(dphi)


spiral(0.001, 90)

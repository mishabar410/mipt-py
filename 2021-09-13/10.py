#десятб (цветочек)

import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed('fastest')


def mnogoug(n, l, alpha):
    angle = 180 - 180 * (n - 2) / n
    turtle.setheading(alpha)
    for i in range(1, n + 1, 1):
        turtle.forward(l)
        turtle.left(angle)


for i in range(1, 6):
    mnogoug(50, 10, i * 360 / 5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

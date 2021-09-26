import turtle
import numpy as np
import math
turtle.shape('turtle')
turtle.speed('fastest')


def mnogoug(n, l, alpha):
    angle = 180 - 180 * (n - 2) / n
    turtle.setheading(alpha)
    for i in range(1, math.floor(n / 2) + 2, 1):
        turtle.forward(l)
        turtle.left(angle)


for _ in range(20):
    mnogoug(30, 5, 90)
    mnogoug(30, 1, 270)

#девятб (многоуголники)

import turtle
import numpy as np
turtle.shape('turtle')
# turtle.speed('fastest')


def mnogoug(n, l, alpha):
    angle = 180 - 180 * (n - 2) / n
    turtle.setheading(alpha)
    for i in range(1, n + 1, 1):
        turtle.forward(l)
        turtle.left(angle)


for i in range(3, 10):
    R = i * 10 / np.sin(np.pi / i)
    turtle.penup()
    turtle.setx(R)
    turtle.sety(0)
    turtle.pendown()
    mnogoug(i, i * 20)

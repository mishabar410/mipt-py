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
    R = i*20/np.sin(3.14/i)*0.75
    turtle.penup()
    # turtle.setx(-R*np.cos(6.28/i))
    # turtle.sety(-R*np.sin(6.28/i))
    turtle.setx(R**np.cos(3.14/2 * (1- 1/i))+10*i)
    turtle.sety(R**np.sin(3.14/2 * (1- 1/i))-10*i)
    turtle.pendown()
    mnogoug(i, i * 20, 180)

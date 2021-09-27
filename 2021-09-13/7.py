#сем (спирал)

import turtle
turtle.shape('turtle')
turtle.speed('fastest')


def spiral(a, dphi):
    for i in range(1, 200, 1):
        turtle.forward(a * dphi * (1 + (i * dphi)**2)**0.5)
        turtle.left(dphi)
        print((turtle.xcor()**2 + turtle.ycor()**2)**0.5/i/dphi)


spiral(0.001, 10)
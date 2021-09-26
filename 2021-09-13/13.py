# тринадцатб :)

import turtle
import numpy as np
import math
turtle.shape('turtle')
turtle.speed('fastest')

# color()   Установить цвет
# begin_fill()  Необходимо вызвать перед рисованием фигуры, которую надо закрасить
# end_fill()    Вызвать после окончания рисования фигуры


def mnogoug(n, l, alpha, decimal):
    angle = 180 - 180 * (n - 2) / n
    turtle.setheading(alpha)
    for i in range(1, math.floor(n * decimal) + 1, 1):
        turtle.forward(l)
        turtle.left(angle)


turtle.color('yellow')
turtle.begin_fill()
mnogoug(100, 3, 0, 1)
turtle.end_fill()
turtle.color('blue')
turtle.penup()
turtle.goto(20, 50)
turtle.pendown()
turtle.begin_fill()
mnogoug(100, 0.5, 0, 1)
turtle.end_fill()
turtle.penup()
turtle.goto(-20, 50)
turtle.pendown()
turtle.begin_fill()
mnogoug(100, 0.5, 0, 1)
turtle.end_fill()
turtle.penup()
turtle.goto(-15, 20)
turtle.width(5)
turtle.pendown()
turtle.color('red')
mnogoug(100, 0.9, -90, 0.5)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.width(5)
turtle.color('black')
turtle.goto(0, 30)

turtle.done()

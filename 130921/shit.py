
#три
# import turtle
# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)


#четыре
#import turtle
# turtle.shape('turtle')
# for i in range(1, 101, 1):
# 	turtle.forward(10)
# 	turtle.left(7.5)


#пят
# def square(a):
# 	turtle.setheading(90)
# 	turtle.forward(a)
# 	turtle.left(90)
# 	turtle.forward(a)
# 	turtle.left(90)
# 	turtle.forward(a)
# 	turtle.left(90)
# 	turtle.forward(a)
# 	turtle.penup()
# 	turtle.home()
# 	turtle.pendown()
# turtle.shape('turtle')
# for i in range(10, 101, 10):
# 	turtle.penup()
# 	turtle.setx(i/2)
# 	turtle.sety(-i/2)
# 	turtle.pendown()
# 	square(i)
# 	turtle.penup()

#шест (павук)

# import turtle
# turtle.shape('turtle')

# def  pavuk(a):
# 	for i in range(1, a+1, 1):
# 		angle = 360/a
# 		turtle.forward(50)
# 		turtle.left(180)
# 		turtle.forward(50)
# 		turtle.left(180 + angle)

# pavuk(10)

#сем (спирал)



# import turtle
# turtle.shape('turtle')
# turtle.speed('fastest')
# def spiral(a, dphi):
# 	for i in range(1, 1000, 1):
# 		turtle.forward(a*dphi*(1+(i*dphi)**2)**0.5)
# 		turtle.left(dphi)
# spiral(0.001, 10)


#во сем (спирал квадратб)

# import turtle
# turtle.shape('turtle')
# turtle.speed('fastest')
# 
# def spiral(a, dphi):
# 	for i in range(1, 1000, 1):
# 		turtle.forward(a*dphi*(1+(i*dphi)**2)**0.5)
# 		turtle.left(dphi)
# spiral(0.001, 90)

#девятб (многоуголники)

# import turtle
# import numpy as np
# turtle.shape('turtle')
# # turtle.speed('fastest')

# def mnogoug(n, l, alpha):
# 	angle = 180 - 180*(n-2)/n
# 	turtle.setheading(alpha)
# 	for i in range(1, n+1, 1):
# 		turtle.forward(l)
# 		turtle.left(angle)

# for i in range(3, 10):
# 	R = i*10/np.sin(np.pi/i)
# 	turtle.penup()
# 	turtle.setx(R)
# 	turtle.sety(0)
# 	turtle.pendown()
# 	mnogoug(i, i*20)



#десятб (цветочек)

# import turtle
# import numpy as np
# turtle.shape('turtle')
# turtle.speed('fastest')

# def mnogoug(n, l, alpha):
# 	angle = 180 - 180*(n-2)/n
# 	turtle.setheading(alpha)
# 	for i in range(1, n+1, 1):
# 		turtle.forward(l)
# 		turtle.left(angle)

# for i in range(1, 6):
# 	mnogoug(50, 10, i*360/5)
# 	turtle.penup()
# 	turtle.goto(0, 0)
# 	turtle.pendown()

#одиннадцатб (баб очка)

# import turtle
# import numpy as np
# turtle.shape('turtle')
# turtle.speed('fastest')

# def mnogoug(n, l, alpha):
# 	angle = 180 - 180*(n-2)/n
# 	turtle.setheading(alpha)
# 	for i in range(1, n+1, 1):
# 		turtle.forward(l)
# 		turtle.left(angle)

# for i in range(1, 11, 1):
# 	mnogoug(100, i*5, 0)
# 	mnogoug(100, i*5, 180)


#двенадцатб (пружинка)


# import turtle
# import numpy as np
# import math
# turtle.shape('turtle')
# turtle.speed('fastest')

# def mnogoug(n, l, alpha):
# 	angle = 180 - 180*(n-2)/n
# 	turtle.setheading(alpha)
# 	for i in range(1, math.floor(n/2)+1, 1):
# 		turtle.forward(l)
# 		turtle.left(angle)
# for _ in range(20):
# 	mnogoug(30, 5, 0)
# 	mnogoug(30, 1, 180)


#тринадцатб :)

# import turtle
# import numpy as np
# import math
# turtle.shape('turtle')
# turtle.speed('fastest')

# # color() 	Установить цвет
# # begin_fill() 	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
# # end_fill() 	Вызвать после окончания рисования фигуры

# def mnogoug(n, l, alpha, decimal):
# 	angle = 180 - 180*(n-2)/n
# 	turtle.setheading(alpha)
# 	for i in range(1, math.floor(n*decimal)+1, 1):
# 		turtle.forward(l)
# 		turtle.left(angle)

# turtle.color('yellow')
# turtle.begin_fill()
# mnogoug(100, 3, 0, 1)
# turtle.end_fill()
# turtle.color('blue')
# turtle.penup()
# turtle.goto(20, 50)
# turtle.pendown()
# turtle.begin_fill()
# mnogoug(100, 0.5, 0, 1)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-20, 50)
# turtle.pendown()
# turtle.begin_fill()
# mnogoug(100, 0.5, 0, 1)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-15, 20)
# turtle.width(5)
# turtle.pendown()
# turtle.color('red')
# mnogoug(100, 0.9, -90, 0.5)
# turtle.done()

# четырнадцатб (звизда)

import turtle
import numpy as np
import math
turtle.shape('turtle')
turtle.speed('fastest')

def mnogoug(n, l, alpha, decimal, angle):
	turtle.setheading(alpha)
	for i in range(1, math.floor(n*decimal)+1, 1):
		turtle.forward(l)
		turtle.left(angle)

# mnogoug(5, 150, 0, 1, 144)
mnogoug(11, 150, 0, 1, 163.64)
turtle.done()
















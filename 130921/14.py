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

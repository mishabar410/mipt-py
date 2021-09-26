#шест (павук)

import turtle
turtle.shape('turtle')

def  pavuk(a):
	for i in range(1, a+1, 1):
		angle = 360/a
		turtle.forward(50)
		turtle.left(180)
		turtle.forward(50)
		turtle.left(180 + angle) 
pavuk(10)

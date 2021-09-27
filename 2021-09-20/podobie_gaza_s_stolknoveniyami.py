from random import *
import turtle


number_of_turtles = 5
steps_of_time_number = 100


# def move_turtle(unit):
# 	unit.penup
# 	unit.forward(10)

def set_pool(pool):
	for unit in pool:
		unit.penup()
		unit.speed(speed='fastest')
		unit.shape('circle')
		unit.goto(randint(-100, 100), randint(-100, 100))
		unit.left(random()*360)


def move_pool(pool):
	for unit in pool:
		if(unit.xcor() > 200 or  unit.xcor() < -200):
			unit.setheading(180 - unit.heading())
		if(unit.ycor()>200 or unit.ycor()<-200):
			unit.setheading(360 - unit.heading())
	for unit in pool:
		unit.forward(10)
	
	i=0
	for unit in pool:
		if(2*i > number_of_turtles):
			continue
		
		for other_unit in pool:
			if ((unit.xcor()-other_unit.xcor())**2 + ((unit.ycor()-other_unit.ycor())**2) < 900) :
				unit.left(180)
				other_unit.left(180)
		i+=1

	   

 
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]

set_pool(pool)

for i in range(1, 10**6):
	move_pool(pool)
 

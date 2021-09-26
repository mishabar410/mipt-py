

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
		unit.speed(speed='normal')
		unit.goto(randint(-100, 100), randint(-100, 100))
		unit.left(random()*360)


def move_pool(pool):
	for unit in pool:
		if(unit.xcor() > 200 or  unit.xcor() < -200):
			unit.setheading(180 - unit.heading())
		if(unit.ycor()>200 or unit.ycor()<-200):
			unit.setheading(360 - unit.heading())
	for unit in pool:
		unit.forward(30)

	   

 
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]

set_pool(pool)

for i in range(1, 10**6):
	move_pool(pool)

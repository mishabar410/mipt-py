import turtle

turtle.speed(speed=1)
x = 50

postal_numbers  = [((0,0), (0,x), (x/2, x), (x/2, 0), (0, 0)),
						   ((0,x/2), (x/2, x), (x/2,0)),
						   ((0,x), (x/2,x), (x/2, x/2), (0,0), (x/2,0)),
						   ((0, x), (x/2, x), (0,x/2), (x/2, x/2), (0,0)),
						   ((0, x), (0,x/2), (x/2, x/2), (x/2, x), (x/2, 0)),
						   ((x/2, x), (0,x), (0, x/2), (x/2, x/2), (x/2, 0), (0,0)),
						   ((0,0), (0, x/2), (x/2, x), (0, x/2), (x/2, x/2), (x/2,0), (0,0)), 
						   ((0,0), (0,x/2), (x/2, x), (0, x)),
						   ((0,0), (0,x), (x/2, x), (x/2, x/2), (0,x/2), (x/2, x/2), (x/2,0), (0,0)),
						   ((0,0), (x/2, x/2), (x/2, x), (0,x), (0, x/2), (x/2, x/2))]

def postal_draw(N, x, y):
	turtle.penup()
	turtle.goto(x + postal_numbers[N][0][0], y + postal_numbers[N][0][1])
	turtle.pendown()
	for i in postal_numbers[N]:
		turtle.goto(x + i[0], y + i[1])

def index(line):
	num = 1
	for i in line:
		postal_draw(i, num*x, 0)
		num+=1

lines = [0, 1, 2, 3, 4, 5, 6, 7, 8]

data = input()
data = [int(el) for el in data]


index(data)

import turtle

turtle.speed(speed=1)
x = 50

postal_numbers  =         [((0,0), (0,x), (x/2, x), (x/2, 0), (0, 0)),
						   ((0,x/2), (x/2, x), (x/2,0)),
						   ((0,x), (x/2,x), (x/2, x/2), (0,0), (x/2,0)),
						   ((0, x), (x/2, x), (0,x/2), (x/2, x/2), (0,0)),
						   ((0, x), (0,x/2), (x/2, x/2), (x/2, x), (x/2, 0)),
						   ((x/2, x), (0,x), (0, x/2), (x/2, x/2), (x/2, 0), (0,0)),
						   ((0,0), (0, x/2), (x/2, x), (0, x/2), (x/2, x/2), (x/2,0), (0,0)), 
						   ((0,0), (0,x/2), (x/2, x), (0, x)),
						   ((0,0), (0,x), (x/2, x), (x/2, x/2), (0,x/2), (x/2, x/2), (x/2,0), (0,0)),
						   ((0,0), (x/2, x/2), (x/2, x), (0,x), (0, x/2), (x/2, x/2))]

def postal_draw(N, x, y, postal_numbers):
	turtle.penup()
	turtle.goto(x + postal_numbers[N][0][0], y + postal_numbers[N][0][1])
	turtle.pendown()
	for i in postal_numbers[N]:
		turtle.goto(x + i[0], y + i[1])

def index(line, postal_numbers):
	num = 1
	for i in line:
		postal_draw(i, num*x, 0, postal_numbers)
		num+=1

lines = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# data = input()
# data = [int(el) for el in data]
inp = open('input.txt', 'r')
data = inp.readline()
data = data.rstrip()
data = [int(el) for el in data]
inp.close()
inp = open('fonts.txt', 'r')
fonts_raw = []

for i in range(10):
	data = inp.readline()
	data = data.rstrip()
	fonts_raw.append(data)

fonts = []

for line in fonts_raw:
    fonts.append([float(x) for x in line.split()])
newfonts = []

for i in range(len(fonts)):
	newfonts.append([])
	for j in range(len(fonts[i])):
		if j%2==0:
			newfonts[i].append((fonts[i][j], fonts[i][j+1]))

print(newfonts)
#теперь newfonts при наборе можно использовать в точности так, как использовался postal_numbers

index((1,0,0), postal_numbers)



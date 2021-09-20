import turtle

turtle.speed(speed='fastest') 


x = -50
y = 0
Vx = 30
Vy = 30
ay = -10
dt = 0.1
t = 0
for i  in range(10000):
	turtle.goto(x,y)
	if(y<0 and Vy<0):
		Vy = -0.7*Vy
	x += Vx*dt
	y += Vy*dt + ay*dt**2/2
	Vy += ay*dt
	



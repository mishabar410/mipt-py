# пят
def square(a):
    turtle.setheading(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle.shape('turtle')
for i in range(10, 101, 10):
    turtle.penup()
    turtle.setx(i / 2)
    turtle.sety(-i / 2)
    turtle.pendown()
    square(i)
    turtle.penup()

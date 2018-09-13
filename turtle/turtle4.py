import turtle
turtle.shape("turtle")
x = 10
a = 0
for i in range(1,10):
    turtle.setpos(a,a)
    turtle.pendown()
    for j in range (1,5):
        turtle.forward(x)
        turtle.left(90)
    x+=10
    a-=5
    turtle.penup()



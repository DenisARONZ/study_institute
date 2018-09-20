import turtle
import math
r = 30
n = 3
turtle.speed(0)

for i in range (0,30):
        turtle.color("green")
        turtle.pendown()
        turtle.circle(r)
        o = 360/n
        l = 2 * r * math.sin(math.pi/n)
        for j in range (1, n+1):
            turtle.color("blue")
            turtle.setheading(o*j - o/2)
            turtle.forward(l)
            turtle.setheading(o*j)
        turtle.penup()
        turtle.setpos(0.00, 0.00 - r)
        r += 30
        n += 1

        
        




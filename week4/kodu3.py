import turtle
from random import randint

s = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

def sq_turtle(sides, length, s = s, t = t):
    degrees = 360 / sides

    t.begin_poly()
    for i in range(sides):
        print('loop')
        t.fd(length)
        t.lt(degrees)
    t.end_poly()

t.penup()
for i in range(30):
    t.setpos(randint(-500, 500), randint(-500, 500))
    t.pendown()
    sq_turtle(randint(3, 10), randint(10, 50))
    t.penup()


s.exitonclick()
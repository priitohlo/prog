import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.fd(300)
t.left(40)
t.fd(40)
t.left(140)
t.fd(360)
t.left(140)
t.fd(40)

t.penup()

t.left(180)
t.fd(40)
t.rt(140)
t.fd(180)
t.lt(90)

t.pendown()

t.fd(300)
t.rt(120)
t.color("red")
t.begin_fill()
t.fd(50)
t.rt(120)
t.fd(50)
t.end_fill()
t.lt(60)

t.penup()

t.fd(20)
t.lt(20)

t.pendown()

t.color("black")
t.fd(200)
t.rt(110)
t.fd(68)
t.begin_fill()
t.color("green")
t.fd(90)
t.rt(120)
t.fd(180)
t.end_fill()

s.exitonclick()
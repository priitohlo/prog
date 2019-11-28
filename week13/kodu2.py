import turtle

def turtle_fractal(depth, length = 90):
    global s, t
    
    for i in range(3):
        t.fd(length)
        if depth == 1:
            t.rt(90)
        else:
            t.lt(90)
            turtle_fractal(depth - 1, length / 2)
            t.lt(90)
    t.fd(length)


s = turtle.Screen()
t = turtle.Turtle()

turtle_fractal(4)

s.exitonclick()
import turtle
from random import randint

s = turtle.Screen()
t = turtle.Turtle()

idx = 0

with open('lisa/lisa1.txt', 'r', encoding='utf-8') as f:
    for r in f:
        try:
            idx += 1
            print(idx)
            cmd = r.strip()
            if cmd == 'mine_otse':
                repeat = int(next(f))
                idx += 1
                t.fd(15 * repeat)
            elif cmd == 'pööra_vasakule':
                degrees = int(next(f))
                idx += 1
                t.lt(degrees)
            elif cmd == 'tõsta_pastakas':
                t.penup()
            elif cmd == 'langeta_pastakas':
                t.pendown()
            elif cmd == 'joonista_kaar':
                radius = int(next(f))
                degrees = int(next(f))
                idx += 2
                t.circle(radius * 15, degrees)
            elif cmd == 'joonista_hulknurk':
                sides = int(next(f))
                length = int(next(f))
                idx += 2
                if sides == 3:
                    degrees = 180 / sides
                elif sides > 3:
                    degrees = 360 / sides
                t.begin_poly()
                for i in range(sides):
                    t.fd(length)
                    t.lt(degrees)
                t.end_poly()
            else:
                raise Exception('Tekstifail on vigane. Real ' + str(idx) + ' asub tundmatu käsklus.')
        except Exception as e:
            print(e)
            pass

s.exitonclick()
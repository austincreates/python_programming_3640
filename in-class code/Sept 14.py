import turtle
import math

#print (austin)
"""austin.fd(100)
austin.lt(90)
austin.fd(100)"""

"""def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)"""

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def newsquare(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)
    """for i in range(n):
        t.fd(length)
        t.lt(angle)"""

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)
    """circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)"""

    """for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)"""

"""def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)"""

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()
i = turtle.Turtle()

a.rt(30)
b.lt(60)
c.lt(150)
d.lt(240)
polygon(a, 3, 200)
polygon(b,3, 200)
polygon(c, 3, 200)
polygon (d, 3, 200)
e.rt(30)
e.fd(200)
e.lt(120)
e.fd(98.5)
f.lt(60)
f.fd(200)
f.lt(120)
f.fd(98.5)
g.lt(150)
g.fd(200)
g.lt(120)
g.fd(98.5)
h.lt(240)
h.fd(200)
h.lt(120)
h.fd(98.5)

circle(e, 58)
circle(f, 58)
circle(g, 58)
circle(h, 58)

i.rt(30)
i.fd(200)
i.lt(90)
#i.fd(100)
circle(i, 200)


turtle.mainloop()
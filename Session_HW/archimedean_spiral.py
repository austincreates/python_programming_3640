import turtle
import math


a = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

def spiral(t, loops):
    #t.lt()
    r = 1
    angle = 90
    for i in range(loops):
        arc(t, r, angle)
        r += 1
        if angle >1:
            angle -= 1
        else:
            angle = angle/2
        
        
        
        

spiral(a, 1000)

turtle.mainloop()


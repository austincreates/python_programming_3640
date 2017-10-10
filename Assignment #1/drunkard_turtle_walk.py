import turtle
import random

drunk = turtle.Turtle()
def drunk_walk(t, n):
    choices = []
    forward= "fwd"
    back = "back"
    left = "left"
    right = "right"
    for num in range(n + 1):
        rand = random.random() * 100
        #print (rand)
        if rand < 25:
           pick = forward
        elif rand < 50:
            pick = back
        elif rand < 75:
            pick = left
        else:
            pick = right 
        choices.append(pick)
        #print (choices)
    for choice in choices:
        if choice == "fwd":
            t.fd(100)
        elif choice == "back":
            t.lt(180)
            t.fd(100)
        elif choice == "left":
            t.lt(90)
            t.fd(100)
        else:
            t.rt(90)
            t.fd(100)

drunk_walk(drunk, 10)
        
turtle.mainloop()
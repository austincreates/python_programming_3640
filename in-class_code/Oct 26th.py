import math
class Point:
    pass;
    

my_point = Point()
my_point

print(type(my_point))
print(isinstance(my_point, Point))

my_point.x = 3
my_point.y = 4

print(my_point.x)
print(my_point.y)
x = my_point.y
print(x)
print(my_point.x)

print ('{} {}'.format(my_point.x, my_point.y))
distance = math.sqrt(my_point.x**2 + my_point.y**2)
print(distance)


class Rectangle:
    pass;

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def print_point(p):
    print('({}, {})'.format(p.x, p.y))
    
center = find_center(box)
print_point(center)

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width)
print(box.height)
print('grow')
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)

p1 = Point()
p1.x = 3.0
p1.y = 4.0

import copy
p2 = copy.copy(p1)

print_point(p1)
print_point(p2)

print(p1 is p2)
print(p1 == p2)


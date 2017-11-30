import math
class Point:
    pass;
class Circle:
    pass;
class Rectangle:
    pass;

def print_point(p):
    print('({}, {})'.format(p.x, p.y))

#def return_point(p):
#    return

box = Rectangle()
box.width = 200
box.height = 50
box.corner = Point()
box.corner.x = -125
box.corner.y = -75

def find_corners(rect):
    corners = []
    c1 = Point()
    c2 = Point()
    c3 = Point()
    c1.x = rect.corner.x 
    c1.y = rect.corner.y + rect.height
    c2.x = rect.corner.x + rect.width
    c2.y = rect.corner.y
    c3.x = rect.corner.x + rect.width
    c3.y = rect.corner.y + rect.height
    corners.append(c1)
    corners.append(c2)
    corners.append(c3)
    return corners

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
center = find_center(box)
print_point(center)

my_point = Point()
my_point.x = -40
my_point.y = 75
attr1 = Circle()
attr1.center = Point()
attr1.center.x = 150
attr1.center.y = 100
attr1.radius = 75

def point_in_circle(Circle, point):
    if Circle.center.x - Circle.radius <= point.x <= Circle.center.x + Circle.radius:
        if Circle.center.y - Circle.radius <= point.y <= Circle.center.y + Circle.radius:
            return True
    return False

def rect_in_circle(Circle, Rectangle):
    wid = Rectangle.width/2
    hei = Rectangle.height/2
    centa = find_center(Rectangle)
    if Circle.center.x - Circle.radius <= centa.x - wid <= Circle.center.x + Circle.radius:
        if Circle.center.x - Circle.radius <= centa.x + wid <= Circle.center.x + Circle.radius:
            if Circle.center.y - Circle.radius <= centa.y - hei <= Circle.center.y + Circle.radius:
                if Circle.center.y - Circle.radius <= centa.y + hei <= Circle.center.y + Circle.radius:
                    return True
    return False 

def rect_circle_overlap(Circle, Rectangle):
    corn = find_corners(Rectangle)
    for corner in corn:
        if point_in_circle(Circle, corner) == True:
            return True
    if  point_in_circle(Circle, Rectangle.corner) == True:
        return True
    return False
    
    
#print(point_in_circle(attr1, my_point))
#print(rect_in_circle(attr1, box))
print (rect_circle_overlap(attr1, box))
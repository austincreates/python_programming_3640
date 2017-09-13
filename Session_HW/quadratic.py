def quadratic(a, b, c):
    import math
    dis = b**2 - 4*a*c #discriminant is b^2 - 4ac
    sqdis = math.sqrt(dis) #next step is finding sqrt of dis
    """ need two results as consequence of
    adding discriminant to b and subtracting
    discriminant from b"""
    add = (-b + sqdis) / (2 * a)
    sub = (-b - sqdis)/ (2 * a)
    add = round(add, 2)
    sub = round(sub, 2)
    return ("The first result is {} and the second is {}".format(add,sub))

#print(quadratic(10,10,1))

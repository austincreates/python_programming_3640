import math
def mysqrt(a):
    sqrt = a ** (.5)
    return sqrt

def test_square_root(number):
    print ("    a                 sqrt                           modsqrt                          difference")
    for i in range(number):
        a = i + 1
        modsqrt = math.sqrt(a)
        #print (modsqrt)
        sqrt = mysqrt(a)
        #print (sqrt)
        if modsqrt != sqrt:
            dif = abs(modsqrt - sqrt)
        else:
            dif = 0
        
        print ("    {},                {},          {},              {}.".format(a, sqrt, modsqrt, dif))

test_square_root(10)




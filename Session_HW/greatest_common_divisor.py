def gcd(a,b):
    r = a % b #remainer
    if r == 0:
        print("The greatest common divisor is {}".format(min(a, b)))
    elif r == 1:
        print ("The greatest common divisor is 1")
    else:
        return gcd(b, r)

gcd(17, 12)

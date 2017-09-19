def usbmi(height, weight):
    bmi = 703 * weight/(height ** 2)
    if bmi >= 30:
        print ("Your bmi is {:.1f}. You are obese.".format(bmi))
    elif 30 > bmi >= 25:
        print ("Your bmi is {:.1f}. You are overweight".format(bmi))
    elif 25 > bmi > 18.5:
        print ("Your bmi is {:.1f}. You are normal weight".format(bmi))
    else:
        print ("Your bmi is {:.1f}. You are underweight".format(bmi))

h = int(input("Please insert your height here: "))
w = int(input("Please insert your weight here: "))
h = float(h)
w = float(w)
usbmi(h, w)


    
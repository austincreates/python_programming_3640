#Exercise 3

"""num = "1, 2, 3, , , , , 4, 5, 6, 7, 8, 9, 10"
print (num.split(","))
print (num.split(""))
print (num.split(",", 2))
ex = "       super awesome time         "
alpha = "super happy awesome fun time supercalifragelisticexpilodocious"
print (ex.strip(" "))
print (ex)
print (alpha.strip(" superhcious"))
confused = "www.example.com"
print(confused.strip('cmowz.'))
print(ex.replace("s", "f"))
print(ex.replace("s", "f", 1)) """



#exercise 4




def receipt(items):
    items = str(items)
    items = items.lower()
    items = items.split(",")
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    price = 0
    total = 0
    line = 0
    
    for item in items:
        num = 0
        price = 0
        for letter in item:
            num +=1
            if letter in alphabet:
                count = 0
                for alpha in alphabet:
                    if letter != alpha:
                        count += 1
                    else:
                        count += 1
                        price += count
                        
                        if num == len(item):
                            total += price
                            if line == 0:
                                print ("\n")
                                line += 1
                            print("{:^10} ${:.2f}".format(item, price))
                            break

#noticed the hint too late :(
    print ("   Total: ${:.2f}".format(total))
    

                    
myitems = input("Please list grocery items separated by commas: ")
receipt(myitems)


                    

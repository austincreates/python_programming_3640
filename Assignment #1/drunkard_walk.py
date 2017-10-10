import random
def drunk_walk(n):
    total_ver = 0 #total vertical distance
    total_hor = 0 # total horizontal distance
    choices = []
    north = "north"
    south = "south"
    east = "east"
    west = "west"
    for num in range(n + 1):
        rand = random.random() * 100
        #print (rand)
        if rand < 25:
           pick = north
        elif rand < 50:
            pick = south
        elif rand < 75:
            pick = east
        else:
            pick = west 
        choices.append(pick)
        #print (choices)
    for choice in choices:
        if choice == "north":
            total_ver += 100
            #print ("Total ver {}".format(total_ver))
        elif choice == "south":
            total_ver -= 100
        elif choice == "east":
            total_hor += 100
        else:
            total_hor -= 100
        #print ("Total ver" , total_ver)
        #print ("Total hor" , total_hor)
    if total_ver == 0:
        total_hor = int(total_hor)
        return ("Distance from origin is {}".format(total_hor))
    elif total_hor == 0:
        total_ver = int(total_ver)
        return ("Distance from origin is {}".format(total_ver))
    else:
        distance = ((abs(total_ver ** 2)) + (abs(total_hor ** 2))) ** .5
        return ("Distance from origin is {}".format(distance))

print(drunk_walk(10))

        
        

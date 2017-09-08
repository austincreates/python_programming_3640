#Assignment #1
#Exercise 2.1
print ((42*60) + 42, "seconds")
#Exercise 2.2
print (10/1.61, "miles")
#Exercise 2.3
#assuming we are only using skills learned in-class
""" print ((42*60) + 42) #total seconds
print (10/1.61) #amount of miles
print (2562/(10/1.61)) #determines seconds per mile
print (412.482/60) #determines amount of minutes (indicated by number before decimal place)
print (((((412.482/60) - 6)*100)/100)*60) #determines amount of seconds """
print ("6 minute 52 second walking pace")
""" print ((60*6) + 52) #seconds ran per mile
print (60*60) #seconds ran per hour """
print (3600/412, "miles per hour")

#exercise 1.1
pi = 3.14159265358997931
r = 5
v = 4/3*pi*r**3
print ("The volume of a sphere with radius 5 is {:.2f}.".format(v)) 

#exercise 1.2
cp = 24.95 #coverprice
dis = .4 #discount
ship = 3 #shipping cost
add = .75 #cost of additional copy
copy = 60 #copies purchased
total = (copy*cp) * (1-dis) + 3 + (copy - 1) * add
total = round (total, 2)
print("$", total, "is total wholesale cost of books")

#exercise 1.3
start_time_hr = 6 + 52/60
easy_pace_hr = (8 + 15/60)/60
tempo_pace_hr = (7+ 12/60)/60
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr - int(breakfast_hr)) * 60
breakfast_sec = (breakfast_min - int(breakfast_min)) * 60

print('Breakfast time is {:02d}:{:02d}:{:02d}.'.format(
    int(breakfast_hr),
    int(breakfast_min),
    int(breakfast_sec)))
#exercise 1.4
increase = (89/82 - 1) * 100
#print (increase)
print ("The percent increase of the average scores is approximately {:.1f}%." .format (increase))


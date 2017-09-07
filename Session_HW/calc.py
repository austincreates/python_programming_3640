print ((42*60) + 42, "seconds")
print (10/1.61, "miles")
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
pi = 3.14
radius = 5
print ((4/3)* pi * radius **3, "units^3") 
cp = 24.95 #coverprice
dis = .4 #discount
ship = 3 #shipping cost
add = .75 #cost of additional copy
copy = 60 #copies purchased
total = (copy*cp) * (1-dis) + 3 + (copy - 1) * add
total = round (total, 2)
print("$", total, "is total price of books")
ep = (8 * 60) + 15 #easy pace in seconds
tempo = 7 * 60 + 12 #tempo in seconds
total = (2 * ep) + 3 * tempo
#print (total)
minutes = 2286/60
#print (minutes)
# 38 minutes
seconds = .1 * 60
#print (seconds)
new_time_min = 52 + 38 - 60
#print (new_time_min)
new_time_min_secs = new_time_min + seconds/100
print (new_time_min_secs)
print("Therefore, new time is 7:30:06")
increase = (89/82 - 1) * 100
#print (increase)
print ("The percent increase of the average scores is approximately {:.1f}%." .format (increase))


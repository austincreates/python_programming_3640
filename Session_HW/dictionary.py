
#Exercise 1
"""
def histogram(s):
    d = dict()
    for c in s.lower():
        #if c not in d:
            #d[c] = 1
        #else:
            #d[c] += 1 
        #d[c] = d.get(c, 0) + 1
    
    return d

print (histogram("Bookkeeper"))
"""

#Exercise 2
"""
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
#fibArg = 10
#fibArg = 15
#fibArg = 20
fibArg = 25 # results are wow!!!
print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)
"""
#Exercise 3
"""Another example of a global variable would be a Boolean value
that can be manually changed between True and False based on external
events and knowledge outside of the code rather than depending what 
is inside the function itself. """

#Exercise 4.1
def make_dict():
    d = dict()
    lis = []
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        lis.append(word)
    for item in lis:
        d[item] = d.get(item, 0)
    
         
#make_dict()
#Exercise 4.2
def has_duplicates(my_list):
    d = dict()
    for item in my_list:
        if d.get(item, 0) >= 1:
             return True
        d[item] = d.get(item, 0) + 1
         
    return False
    
example = ["a", "b", "c", "d", "e"]

#print d.get("a", 0)

print(has_duplicates(example))
    




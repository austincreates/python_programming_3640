"""fin = open('words.txt')
line = fin.readline()
print(repr(line))  

fin = open('words.txt')
for line in fin:
    word = line.strip() """

"""def find_long_words():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

find_long_words() """

def find_no_e():
    fin = open('words.txt')
    no_e = 0
    e = 0
    for line in fin:
        word = line.strip()
        if "e" not in word:
            no_e += 1
        else:
            e +=1
            #print (word)
    print ((no_e/(no_e + e))*100)

find_no_e() 

"""def if_e (submission):
    fin = open('words.txt')
    fin = str(fin)
    if submission in fin:
        if "e" not in submission:
            print ("True")
        else:
            print ("Fuck You")

if_e("elephant")
        
def has_no_e(word):
    
def find_words_no_e():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if :
            print(word, len(word))

def find_words_no_e():
    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            #print(word)

find_words_no_e()"""

"""def has_no_e (word):
    for letter in word:
        if letter.lower() == 'e':
            return False
    Return True """

def avoids(word, forbidden):
    if forbidden.lower() in word.lower():
        print("False")
    else:
        print("True")
        
    

print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))

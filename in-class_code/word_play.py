#Exercise 1.1
"""
def find_long_words():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

find_long_words()
"""

#Exercise 1.2
"""def no_e(choice):
    choice = choice.lower()
    if "e" not in choice:
        return (True)
    else:
        return (False) """

#print(no_e("tally"))

#Exercise 1.2.1
"""
def percentage_e():
    fin = open('words.txt')
    amount = 0
    total = 0

    for line in fin:
        word = line.strip()
        if "e" not in word:
            amount += 1
            total += 1
           #print (word)
        else:
            total += 1
        
    print (amount / total )

percentage_e()
"""
#Exercise 1.3
"""
def avoids(word, letters):
    word = word.lower()
    letters = letters.lower()
    for letter in letters:
        if letter in word:
            return False

    return True

print(avoids("fsajdqpreoijewoiljfsa", "q"))
"""
#Exercise 1.3.1
"""
def forbidden(letters):
    count = 0
    length = len(letters)
    finish = 0
    letters = letters.lower()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        finish = 0
        for letter in letters:
            if letter in word:
                break;
            else:
                finish += 1
            if finish == length:
                count += 1
    print (count)

forbidden("abcde")
"""
#Exercise 1.4.1
"""
def uses_only(word, letters):
    word = word.lower()
    letters = letters.lower()
    for letter in word:
        if letter in letters:
            break;
        else: 
            return (False)
    return (True)

print(uses_only("Mississippi", "fonwapewnp9iwjip"))
"""        
#Exercise 1.5
"""
def uses_all(word, letters):
    for each in letters:
        if each not in word:
            return (False)
    return (True)
            

print(uses_all("elephat", "eephant"))
"""
#Exercise 1.6
"""
def is_abecedarian(word):
    previous = word[0]
    for letter in word:
        if ord(letter) < ord(previous):
            return (False)
        else:
            previous = letter
    return (True)
        
print(is_abecedarian("aabcccdef"))
"""
"""
#Exercise 2
def is_abecedarian(word, type_num_1):
    previous = word[type_num_1 - 1]
    current = word[type_num_1]
    if ord(current) < ord(previous):
        return (False)
    elif type_num_1 == (len(word) - 1):
        return (True)
    
    else:
        return is_abecedarian(word, type_num_1 + 1)

print(is_abecedarian("elephant", 1))
"""

def is_abecedarian(word):
    num = 0
    previous = word[num]
    current = word[num + 1]
    while ord(current) <!  ord(previous):
        num +=1
        if num == len(word):
            return True

    return False 

print(is_abecedarian("elephant"))

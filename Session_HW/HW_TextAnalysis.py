import string
import random
#Exercise 1 - 4, 6

def process_file(text, name, word_list):
    count = 0
    d = dict()
    punc = string.punctuation
    fin = open(text)
    for line in fin:
        line = line.strip()
        for item in punc:
            line = line.replace(item, "")
        line = line.lower()
        words = line.split()
        limit = 5
        for word in words:
            if word == name.lower():
                count += 1
        if count >= limit:
            for word in words:
                d[word] = d.get(word, 0) + 1
    
    new_count = 0   
    for key in d.items():
        new_count += 1
    lis = []
    for i in range(19):
        val = 0
        highest = ""
        for key,value in d.items():
            if key not in lis:
                if value > val:
                    highest = key
                val = d[key]
        lis.append(highest)
    
    
        
    print(d)
    print("The amount of words is: " , new_count)
    print("The most frequent words are: " , lis)
    new_fin = open(word_list)
    new_lis = []
    for newline in new_fin:
        newline = newline.strip()
        newline = newline.lower()
        newwords = newline.split()
        for word in newwords:
            if word not in d:
                new_lis.append(word)
    print(new_lis)
    t = []
    for key, value in d.items():
        t.extend([key] * value)
    print (random.choice(t))


#Exercise 5

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)


            
process_file("Dracula.txt", "Dracula", "words.txt" )





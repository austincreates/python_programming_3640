team = 'New England Patriots'

letter = team[0]
print(len(team))

print(team[len(team)-1])
print(team[-1])

for letter in team:
    if letter.isalpha():
        print (letter)





prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter != "Q" and letter != "O":
        print (letter + suffix)
    else:
        print(letter + 'u' + suffix)

print(team[0:11])
print(team[12:20])
print(team[:11])
print(team[12:])
print(team[:-1])
print(team[::-2])

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

def count(word, letter ):
    add = 0
    for i in word:
        i = i.lower()
        if i in letter:
            
            add += 1
    return add

print(count("Peter Piper picked a pepper", "p"))

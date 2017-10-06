AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
# print(AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'
print(AFC_east)

print('Buffalo bills' in AFC_east)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[1][2][1])
for team in AFC_east:
    print (team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

t = ['a', 'b', 'c', 'd']
t.append('e')
print(t)
a = [1 , 2, 3]
t.extend(a)
print(t)
t.insert(2, 'Winfred')
print(t)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
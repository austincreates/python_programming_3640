names = ['Julian','Zach', 'Alex']
scores = [95, 75, 85]

def histogram(s):
    d = dict()
    for c in s.lower():
        """if c not in d:
            d[c] = 1
        else:
            d[c] += 1 """
        d[c] = d.get(c, 0) + 1
    
    return d

def print_hist():
    for c in h:
        print (c, h[c])
h = (histogram('Bookkeeper'))
print (h)
print(sorted(h))

print(h.get('o'))

print_hist()
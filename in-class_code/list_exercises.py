#Exercise 1
"""
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

#Apple
print (L[0][0])
#Lisa
print (L[2][2])
#On Rail
print (L[1][2][1])
"""
#Exercise 2
"""
t = ['a', 'b', 'c']

t.append('d')

print (t)
t.extend([1, 2 , 3])
print (t)

s = ['z', 'y', 'x', 'u', 'v', 'q']
s.sort()
print(s)
"""

#Exercise 3
def nested_sum(t):
    sum = 0
    for lis in t:
        for ist in lis:
            sum += ist
    return sum


def cumsum(t):
    sum = 0
    for i in range(len(t)):
        sum += t[i]
        t[i] = sum
    print (t)

    
    """
    Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    
    return
"""



def middle(t):
    new_t = []
    for element in t:
        if element is not t[0] and element is not t[-1]:
            new_t.append(element)
    
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return new_t


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.remove(t[0])
    t.remove(t[-1])
    return t


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    s = []
    for element in t:
        s.append(element)
    s.sort()
    if t == s:
        return (True)
    else:
        return (False)
    


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    lis = []
    if len(word1) != len(word2):
        return (False)
    for element in word2:
        lis.append(element)
    for i in word1:
        lis.remove(i)
    if lis == []:
        return (True)
    else:
        return (False)
        
    return


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    lis = []
    for letter in s:
        lis.append(letter)
    for letter in s:
        lis.remove(letter)
        if letter in lis:
            return True
        else: 
            return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    lis = []
    for letter in s:
        lis.append(letter)
    check = lis[0]
    for element in lis[1:-1]:
        if check == element:
            return (True)
        check = element
    return (False)



def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    cumsum(t)

    t = [1, 2, 3, 4]
    print(middle(t))
    print(chop(t))
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

    print(has_adjacent_duplicates('abracadabra'))
    print(has_adjacent_duplicates('abracaddabra'))
if __name__ == '__main__':
    main()

"""

#Exercise 4
def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if x == my_list[mid]:
            return mid
        elif x < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

"""
#Exercise 4

def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    left = 0
    right = len(my_list) - 1
    while left <= right:
        middle = ((left + right) / 2)
        middle = int(middle)
        if x == my_list[middle]:
            return middle
        elif x > my_list[middle]:
            left = middle + 1
        else:
            right = middle - 1


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
def is_palindrome(word):
    print(word)
    print(len(word))
    if len(word) < 2:
        pass;
    elif len(word) == 2 and word[0] == word[-1]:
        pass;
    else: 
        if word[0] == word[-1]: 
            is_palindrome(word[1:-1])
        else:
            return False
    return True

print (is_palindrome("jujuj"))
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999
    Returns: a string that is the number in Chinese
    '''
    number2 = str(number)
    number_list = []
    for digit in (number2):
        number_list.append(digit)
    if 0 <= number <= 10:
        result = trans[number2]
        return result
    elif 11 <= number <= 19:
        result = trans["10"] + " " + trans[number_list[1]] 
        return result
    elif 20 <= number <= 99:
        if number_list[1] == "0":
            result = trans[number_list[0]] + " " + trans["10"]
            return result 
        else:
            result = trans[number_list[0]] + " " + trans["10"]
            for num in range(len(number_list)):
                if num != 0:
                    result += " " + trans[number_list[num]]
                    return result
    elif number == 100:
        result = trans[100]
        return result
    elif 101 <= number <= 999:
        result = trans[number_list[0]] + " " + trans["100"]
        if number_list[1] == "0" and number_list[2] == "0":
            return result
        elif number_list[1] == "0":
            for i in range(len(number_list)):
                if i != 0:
                    if i == 1:
                        result += " " + trans["0"]
                    else:
                        result += " " + trans[number_list[i]]
            return result
        else:
            for i in range(len(number_list)):
                if i != 0:
                    if i == 1:
                        result += " " + trans[number_list[i]] + " " + trans["10"]
                        
                    else:
                        result += " " + trans[number_list[i]]
                        
            return result


# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()


def find_factors(integer):
    factors = []
    while integer > 1 :
        for num in range (2, integer + 1):
            if integer % num == 0:
                integer = int(integer/num)
                factors.append(num)
                break;
    return factors
   
            
                
print(find_factors(150))
    
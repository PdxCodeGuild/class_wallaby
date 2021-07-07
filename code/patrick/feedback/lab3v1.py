
given_number = int(input('Enter a number: '))
tens_digit = given_number//10
ones_digit = given_number%10

ones_digit = str(ones_digit)
Dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}


def base(here):
    if len(str(given_number)) == 1 and given_number == 0:
        return 'zero'
    elif given_number in range(1, 9):
        return(Dict[ones_digit])
    elif given_number in range(1, 21):
        if given_number == 10:
            return('ten')
        elif given_number == 11:
            return('eleven')
        elif given_number == 12:
            return('twelve')
        elif given_number == 13:
            return('thirteen')
        elif given_number == 14:
            return('fourteen')
        elif given_number == 15:
            return('fifteen')
        elif given_number == 16:
            return('sixteen')
        elif given_number == 17:
            return('seventeen')
        elif given_number == 18:
            return('eighteen')
        elif given_number == 19:
            return('nineteen')    
        elif given_number == 20:
            return('twenty')
    elif given_number in range(21,30):
        return(f'twenty {Dict[ones_digit]}')
    elif given_number in range(30,40):
        return(f'thirty {Dict[ones_digit]}')
    elif given_number in range(40,50):
        return(f'fourty {Dict[ones_digit]}')
    elif given_number in range(50,60):
        return(f'fifty {Dict[ones_digit]}')
    elif given_number in range(60,70):
        return(f'sixty {Dict[ones_digit]}') 
    elif given_number in range(70,80):
        return(f'seventy {Dict[ones_digit]}')
    elif given_number in range(80,90):
        return(f'eighty {Dict[ones_digit]}')        
    elif given_number in range(90,100):
        return(f'ninety {Dict[ones_digit]}') 
    

key_errors = []
if given_number in range(0, 100):
    try:
        print(base(given_number))
    except KeyError:
        key_errors.append(given_number)
print(key_errors)
  
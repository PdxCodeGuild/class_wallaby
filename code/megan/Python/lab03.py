ones_dict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens_dict = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

tens_dict = {
    0: '',
    1: 'ten',
    2: 'twenty-',
    3: 'thirty-',
    4: 'forty-',
    5: 'fifty-',
    6: 'sixty-',
    7: 'seventy-',
    8: 'eighty-',
    9: 'ninety-'
}

user_num = int(input("Enter a number between 0-999: "))

hundreds_digit = user_num // 100
tens_digit = user_num % 100 // 10
ones_digit = user_num % 10

def num_to_phrase(num):
    if user_num == 0:
        return 'zero'
    hundreds_digit = user_num // 100
    tens_digit = user_num % 100 // 10
    ones_digit = user_num % 10

    hundreds = ones_dict[hundreds_digit]
    tens = tens_dict[tens_digit]
    ones = ones_dict[ones_digit]

    if hundreds_digit == 0:
        if tens_digit == 1:
            return teens_dict[ones_digit]
        return f'{tens}{ones}'

    if tens_digit == 1:
        return f'{hundreds} hundred {teens_dict[ones_digit]}'
    
    return f'{hundreds} hundred {tens}{ones}'

print(f'{num_to_phrase(user_num)}')
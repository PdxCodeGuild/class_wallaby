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
    9: 'nine',
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
    9: 'ninety-',
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

# test_num = 123
# hundreds_digit = test_num // 100
# tens_digit = test_num % 100 // 10
# ones_digit = test_num % 10

# print(hundreds_digit, tens_digit, ones_digit)

def translator(num):
    if num == 0:
        return 'zero'
    hundreds_digit = num // 100
    tens_digit = num % 100 // 10
    ones_digit = num % 10

    hundreds = ones_dict[hundreds_digit]
    tens = tens_dict[tens_digit]
    ones = ones_dict[ones_digit]

    if hundreds_digit == 0:
        if tens_digit == 1:
            return teens_dict[ones_digit]
        return f'{tens}{ones}'.strip('-')

    if tens_digit == 1:
        return f'{hundreds} hundred {teens_dict[ones_digit]}'
    
    return f'{hundreds} hundred {tens}{ones}'.strip('-').strip()
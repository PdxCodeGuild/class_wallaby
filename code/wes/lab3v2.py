# Dictionary for 100-900
hundereds_digit = {

    100 : "one hundred",
    200 : "two hundered",
    300 : "three hundred",
    400 : "four hundred",
    500 : "five hundred",
    600 : "six hundred",
    700 : "seven hundred",
    800 : "eight hundred",
    900 : "nine hundred",

}

# Dictionary for 10-90 & 11-19
tens_digit = {

    0 : '',
    1 : 'ten',
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty', 
    5 : 'fifty',
    6 : 'sixty',
    7 : 'sevinty',
    8 : 'eighty',
    9 : 'nintey',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',

}

# Dictionary for 0-9
ones_digit = {

    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
}

# Ask's user to input a number
user_input = input("Please enter a number: ")

# Converts the users input to a integer
user_input = int(user_input)


# Flooor divides user_input and multiplies by 100 and stores it in hundreds_math variable
hundereds_math = user_input // 100 * 100

# Preforms modulus on user_input and stores it in tens_math1 variable
tens_math1 = user_input % 100

# Preforms modulus on user_input and floor divides by 10 & stores it in tens_math1 variable
tens_math = user_input % 100 // 10

# Preforms modlus on user_input and stores it in ones_math variable
ones_math = user_input % 10



if tens_digit and ones_digit == 0:
    print(hundereds_digit[user_input])

elif tens_math1 == 11:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 12:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 13:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")    
elif tens_math1 == 14:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 15:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 16:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")    
elif tens_math1 == 17:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 18:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")
elif tens_math1 == 19:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math1]}")

else:
    print(f"{hundereds_digit[hundereds_math]} {tens_digit[tens_math]}{ones_digit[ones_math]}")




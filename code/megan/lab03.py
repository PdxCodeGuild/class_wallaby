# Lab 03: Number to Phrase

# create dictionary for number-value pairs
num_to_phrase = { # easier to use multiple dictionaries?
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

# ask for user input (do I need to do this?)
user_num = int(input("Enter a number between 0-999: "))

# convert user input into an integer
# user_num = int(user_num)

# extract ones and tens digits




# run a loop to convert user entered number into phrase
#while True:
    #if num_to_phrase == 'done':
        #print("\nGoodbye!")
        #break 

if user_num < 20:
    print(num_to_phrase[user_num])

elif user_num >= 20 and user_num < 100: #shorthand
    tens_digit = user_num // 10
    print(f"{tens_digit}0")
    ones_digit = user_num % 10
    print(f"{ones_digit}")
    if tens_digit > 1:
        print(f"{num_to_phrase[tens_digit]}-{num_to_phrase[ones_digit]}")
        # print(num_to_phrase[tens_digit] + num_to_phrase[ones_digit])
    # elif tens_digit == 0:
        # print(f"{num_to_phrase[user_num]}-{num_to_phrase[user_num]}")

elif user_num >= 100 and user_num < 1000:    
    hundreds_digit = user_num // 100
    print(f"{hundreds_digit} hundred")
    tens_digit = user_num // 10
    ones_digit = user_num % 10
    if hundreds_digit != 0:
        print(f"{num_to_phrase[hundreds_digit]} ")
    elif hundreds_digit == 0:
        print(f"{num_to_phrase[tens_digit]}-{num_to_phrase[ones_digit]}")
    if tens_digit != 0:
        print(f"{num_to_phrase[tens_digit]}-{num_to_phrase[ones_digit]}")
    elif tens_digit == 0:
        print(f"{num_to_phrase[user_num]} hundred {num_to_phrase[tens_digit]}-{num_to_phrase[user_num]}")
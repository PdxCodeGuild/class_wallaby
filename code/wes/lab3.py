

tens_digit = {

    0 : 'zero',
    1 : 'ten',
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty', 
    5 : 'fifty',
    6 : 'sixty',
    7 : 'sevinty',
    8 : 'eighty',
    9 : 'nintey',

}

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

teens = {
    10 : 'ten',
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


user_input = input("Please enter a number: ")

user_input = int(user_input)

#total = tens_digit + ones_digit


tens_math = user_input//10
ones_math = user_input%10


if user_input < 1:
    print("zero")

elif user_input <= 9:
    print(ones_digit[user_input])

elif user_input == 10:
    print(teens[user_input])    

elif user_input == 11:
    print(teens[user_input])

elif user_input == 12:
    print(teens[user_input])
        
elif user_input == 13:
    print(teens[user_input])

elif user_input == 14:
    print(teens[user_input])

elif user_input == 15:
    print(teens[user_input])    

elif user_input == 16:
    print(teens[user_input])

elif user_input == 17:
    print(teens[user_input])

elif user_input == 18:
    print(teens[user_input])

elif user_input == 19:
    print(teens[user_input])

else:
    print(f"{tens_digit[tens_math]}-{ones_digit[ones_math]}")


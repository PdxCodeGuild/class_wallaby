digit10 = {
'1': 'ten',
'2': 'twenty',
'3': 'thirty',
'4': 'forty',
'5': 'fifty',
'6': 'sixty',
'7': 'seventy',
'8': 'eighty',
'9': 'ninety',

}
digit1 = {
     '1': 'one',
     '2': 'two',
     '3': 'three',
     '4': 'four',
     '5': 'five',
     '6': 'six',
     '7': 'seven',
     '8': 'eight',
     '9': 'nine'
}

#user = input("Enter number: ")
number_word1 = digit1.get('2')
#print(number_word1)
number_word2 = digit10.get('2')
print(number_word2)

print(f'{number_word2}-{number_word1}')






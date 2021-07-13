card_number = input('Enter the 16 digit credit card number: ')
number = map(int, card_number)
number_1 = list(number)
check_digit = number_1.pop(-1)
number_2 = reversed(number_1)
number_2 = list(number_2)
final = []

for i in range(len(number_2)):
    if i % 2 == 1:
        final.append(number_2[i])

    elif i % 2 == 0:
        x = number_2[i] * 2
        if x > 9:
            x = x - 9  
        final.append(x)

sum = 0
for i in final:
    sum += i

ones_digit = sum%10
if ones_digit == check_digit:
    print("valid")
else:
    print('try again')
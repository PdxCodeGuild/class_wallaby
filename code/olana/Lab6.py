
#1. Convert the input string into a list of ints
creditcard = "4556737586899855"
#creditcard = input("Please enter credit card numbers: ")
print(list(creditcard)) 

creditcard_as_integers = [int(n) for n in creditcard]

print(creditcard_as_integers)


#2. Slice off the last digit.  That is the **check digit**.
removed_digit = creditcard_as_integers.pop(-1)
print(creditcard_as_integers)
print(removed_digit)


#3. Reverse the digits.
creditcard_as_integers.reverse()
print(creditcard_as_integers)

#4. Double every other element in the reversed list.

double_element =[x * 2 if index % 2 == 0 else x for index, x in enumerate(creditcard_as_integers)]
print(double_element)

#5. Subtract nine from numbers over nine.

subtract_nine = []
for i in range(len(double_element)):
    if double_element[i] > 9:
        subtract_nine.append(double_element[i] - 9)
    else:
        subtract_nine.append(double_element[i])
print(subtract_nine)

#6. Sum all values.
sum_total = sum(subtract_nine)
print(sum_total)

#7. Take the second digit of that sum.
second_digit = sum_total %10
#second_digit = str(sum_total)[-1:]
print(second_digit)
print(removed_digit)
#8. If that matches the check digit, the whole card number is valid.
if removed_digit == second_digit:
    print("Valid!")
else:
    print("Not Valid")


        


test_card_num = '4556737586899855'
# user_input = input('Enter your credit card number for validation: ')

# 1. Convert the input string into a list of ints
test_card_num_list = list(test_card_num)
test_card_num_list = [int(i) for i in test_card_num_list]
print(f"1. {test_card_num_list}")

# 2. Slice off the last digit. That is the check digit.
# test_card_num_list = test_card_num_list[:-1]
check_digit = test_card_num_list.pop(-1)
print(f"2. {test_card_num_list}")

# 3. Reverse the digits.
test_card_num_list.reverse()
print(f"3. {test_card_num_list}")

# 4. Double every other element in the reversed list.
every_other_list = test_card_num_list[:]
every_other_list[::2] = [x*2 for x in every_other_list[::2]]
print(f"4. {every_other_list}")

# 5. Subtract nine from numbers over nine.
subtract_9_list = []

for i in range(len(every_other_list)):
    if every_other_list[i] > 9:
        subtract_9_list.append(every_other_list[i] - 9)
    else:
        subtract_9_list.append(every_other_list[i])

print(f"5. {subtract_9_list}")

# 6. Sum all values.
sum = sum(subtract_9_list)

print(f"6. {sum}")

# 7. Take the second digit of that sum.

# ones_digit = user_num % 10

second_digit = sum % 10
print(second_digit)

# 8. If that matches the check digit, the whole card number is valid.

if second_digit == check_digit:
    print("Valid")
else:
    print("Invalid")
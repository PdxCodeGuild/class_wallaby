test_card_num = '4556737586899855'
# user_input = input('Enter your credit card number for validation: ')

# 1. Convert the input string into a list of ints
test_card_num_list = list(test_card_num)
test_card_num_list = [int(i) for i in test_card_num_list]

print(test_card_num_list)

#for i in range(len(test_card_num_list)):
#    print(test_card_num_list[i]) 

# 2. Slice off the last digit. That is the check digit.
sliced_list = []
test_card_num_list = test_card_num_list[:-1]

print(test_card_num_list)

# 3. Reverse the digits.

reversed_list = []
test_card_num_list.reverse()

print(test_card_num_list)

# 4. Double every other element in the reversed list.
    #slicing?

print(reversed_list[::1*2]) # error

#for i in range(reversed_list): # error
 #   if i % 2 == 0:
  #      reversed_list = reversed_list * 2

#print(test_card_num_list)

# 5. Subtract nine from numbers over nine.

# 6. Sum all values.

# 7. Take the second digit of that sum.

# 8. If that matches the check digit, the whole card number is valid.


"""
# Double every other element in the reversed list.

    # use enumerate?
    # use slice?
    double_every_other_list = reversed_list[::2]
    


if True:
    print('Valid')

    else:
        print('Invalid')
"""
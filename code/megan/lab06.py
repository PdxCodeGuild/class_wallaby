# Lab 06: Credit Card Validation

test_card_num = '4556737586899855'

card_nums_list = []

user_input = (input('Enter your credit card number for validation: ')

# define function

def validation(x): # change x to?
    card_nums_list = user_input
    # convert to ints
    for i in range (len(card_nums)):
        card_nums[i] = int(card_nums[i])
    # convert to list
    ints_list = []
    # .append
   

# Slice off the last digit. That is the check digit.
    sliced_list = []
card_nums = card_nums[:-1]

print(card_nums)
  
# Reverse the digits.
    reversed_list = []
card_nums.reverse() 

print(card_nums)

# Double every other element in the reversed list.

    # use enumerate?
    # use slice?
    double_every_other_list = reversed_list[::2]
    

# Subtract nine from numbers over nine.



# Sum all values.

# Take the second digit of that sum.

# If that matches the check digit, the whole card number is valid.

if True:
    print('Valid')

    else:
        print('Invalid')

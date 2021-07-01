
# Defines a function to keep a running sum of all #'s 
def sum_numbers(numbers):
    counter = 0
    for num in numbers:
        counter += num 
    return counter    

# List of numbers to be included
nums = [5, 0, 8, 3, 4, 1, 6]

#Assigns the function to the nums list
total = sum_numbers(nums)

#Assigns the len operator to get length of the list
length = len(nums)

#Divides the two variables 
length_tot = total / length 


print(length_tot)


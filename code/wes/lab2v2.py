
# Labels function used to get total
def sum_numbers(numbers):
    counter = 0
    for num in numbers:
        counter += num 
    return counter

# Empty array awating user input
nums = []


while True:

    user_number = input("enter a number, or 'done': ")

    if user_number == 'done':
        print(f"average: {length_tot}")
        break

    nums.append(int(user_number))
    total = sum_numbers(nums)

#Assigns the len operator to get length of the list
    length = len(nums)

#Divides the two variables 
    length_tot = total / length 
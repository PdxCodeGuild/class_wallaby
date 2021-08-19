nums = []

while True:
    user_input = input("Enter a number or enter 'done' to quit: ")
    if user_input == 'done':
       break    
    user = int(user_input)
    nums.append(user)
    total = sum(nums)
    print(total /len(nums))
    
   





#hundreds_digit = test_number % 100 // 10 
nums = []
sum = 0




while True:
    user_input = input('enter a number, or "done": ')
    if user_input.isdigit(): # .isdigit idea from https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
        nums.append(user_input)
    elif user_input == 'done':
         for num in nums:
            sum += int(num) 
            average = sum/ len(nums)
            print(average)
            exit()
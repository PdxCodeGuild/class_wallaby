nums = []
sum = 0




while True:
    user_input = input('enter a number, or "done": ')
    if user_input != 'done':
        nums.append(user_input)
        user_input = int(user_input)
        sum += user_input
        continue
    elif user_input == 'done':
        print(nums, sum)
        average = sum/ len(nums)
        print(average)
        break
        
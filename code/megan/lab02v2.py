nums = []

for i in range(len(nums)):
    print(nums[i])

while True:
    usernum = input("Enter a number, or 'done': ")

    if usernum == 'done':
        print(f'Numbers: {nums}')
        avg = sum(nums) / len(nums)
        print(f'Average: {avg}')
        break
    
    else:
        usernum = int(usernum)
        nums.append(usernum)

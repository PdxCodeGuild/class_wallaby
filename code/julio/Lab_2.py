
# loop over the elements

nums = []

for num in nums:

     total_list = sum(nums)

     average_list = total_list /len(nums)
     
while True: 

    num_input = ("enter a number or 'done'  ")

    if num_input == "done":

        print(average_list)

        break

    else: 

        num_input = int(num_input)
        nums.append(num_input)


   

        















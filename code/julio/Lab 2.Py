print("---------------------------------------------------------")
nums_list = []
#--------------------------------------------------------#
while True:
    nums_input = input("enter a number: ")
    if nums_input == 'done' :
        break
 #--------------------------------------------------------#   
    try:
        nums_val = float(nums_input)
    except:
        print('Invalid input')

        continue
    try:
        nums_list.append(int(nums_input))
    except:
        nums_list.append(float(nums_input))
        break
#--------------------------------------------------------#
    nums_total = sum(nums_list)
#--------------------------------------------------------#
print("---------------------------------------------------------")
print(f"average:" , (nums_total /len(nums_list)))
print("---------------------------------------------------------")
print()

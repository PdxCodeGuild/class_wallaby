nums = []


while True:
    user_input =int(input("Enter number: "))
    nums.append(user_input)
    user_choice_to_stop = input("Enter 'done' if want to end or any other key to continue: ")
    total = sum(nums)
    if user_choice_to_stop == "done":
        print(total /len(nums))
        
    
            
            
        
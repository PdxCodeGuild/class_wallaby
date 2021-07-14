'''
Credit Card Validation
Lab 6
7/12/2021
'''

card_number =('4556737586899855') 
card_list = list(card_number)
last_num = int(card_list.pop(-1))
card_list.reverse()



def authinticatorinator(card_list):
    print(card_list)

    for i, num in enumerate(card_list):
      card_list[i] = int(num)

    for i in range(len(card_list)):
            if i % 2 == 0:
        
                card_list[i] = card_list[i]*2
    print(card_list)            
    for i in range(len(card_list)):
        
        if card_list[i] > 9:
            card_list[i] -= 9
    print(card_list)
    sum = 0
    for num in card_list:
        sum += num
    print(sum)

    second_num = int(str(sum)[1])
    print(second_num)

    if second_num == last_num:
        return True
    
    else:
        return False
    
   
if  authinticatorinator(card_list) == True:
     print('Valid!')
else:
    print("Invalid")
    










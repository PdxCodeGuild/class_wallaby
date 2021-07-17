

test = "4556737586899855"



#user_input = input("Please enter card number: ")

def credit_card(card_numbers):
    card_numbers = list(card_numbers)
    card_numbers = [int(index) for index in card_numbers]

    popped_num = card_numbers.pop(-1)

    card_numbers.reverse()
    
    card_numbers = [card_numbers[index] * 2 if index % 2 == 0 else card_numbers[index] for index in 
range(len(card_numbers))]
    card_numbers = [card_numbers[index] - 9 if card_numbers[index] > 9 else card_numbers[index] for index in 
range(len(card_numbers))]
    total = sum(card_numbers)
    if total % 10 == popped_num:
        return True
    else:
        return False
     
card_numbers = input('Enter Credit Card Number: ')
output = 'Card Number Valid!' if credit_card(card_numbers) is True else 'Invalid Card Number! '

print(output)         
       
 
   
    
    


    
print(credit_card(test))




  


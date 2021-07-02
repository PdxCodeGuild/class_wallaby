def sum_numbers(numbers):
        sum_n = 0          
        for x in numbers: 
            sum_n += x
        return sum_n

C_List = []


p_cards = {"A" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
             "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Q" : 10, "K" : 10 }

while True:

    card_1 = input("what's your first card? ")

    

    card_2 = input("what's your second card? ")

    

    card_3 = input("what's your third card? ")

    
    if card_3 == 'done': 
    
        
        break

    C_List.append(card_1)
    C_List.append(card_2)
    C_List.append(card_3)

    print(sum_numbers(C_List))









#--------------------------------------------------------------------------#
deck_list = dict({str(i): i for i in range(2, 11)}, A=1, J=10, Q=10, K=10)
#--------------------------------------------------------------------------#
user_list = []
#----------------------------------------------------------------#
print("----------------------------------------------")
card_1 = deck_list[(input("enter first card: "))]
print("----------------------------------------------")
card_2 = deck_list[(input("enter second card: "))]
print("----------------------------------------------")
card_3 = deck_list[(input("enter third card: "))]
print("----------------------------------------------")
#----------------------------------------------------------------#
user_list.extend([card_1, card_2, card_3])
#----------------------------------------------------------------#
if sum(user_list) == 21:
    print(sum(user_list),":","blackjack")
    print("----------------------------------------------")
elif sum(user_list) > 21: 
    print(sum(user_list),":","bust")
    print("----------------------------------------------")
elif sum(user_list) >= 17:
    print(sum(user_list),":","stay")
    print("----------------------------------------------")
elif sum(user_list) < 17: 
    print(sum(user_list),":", "hit")
    print("----------------------------------------------")  
#----------------------------------------------------------------#
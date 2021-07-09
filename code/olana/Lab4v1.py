# cite: https://www.kite.com/python/answers/how-to-get-a-random-entry-from-a-dictionary-in-python
# cite: https://appdividend.com/2020/06/22/python-random-choice-method-example/

user_card1 = input("What's your first card: ")
user_card2 = input("What's your second card: ")
user_card3 = input("What's your third card: ")

import random
game = []
blackjack_card = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10,'Q':10,'K':10}
blackjack_card_entry = list(blackjack_card.items())
computer = random.choices(blackjack_card_entry,k=3)
#print(computer)

#setup conditions

card1_value = blackjack_card[user_card1]
#print(card1_value)
card2_value = blackjack_card[user_card2]
#print(card2_value)
card3_value = blackjack_card[user_card3]
#print(card3_value)

total = card3_value +card2_value +card1_value
print(total)

if total == 21:
    print("Blackjack!")
elif total <17:
    print("Hit")
elif total>=17:
    print("Stay")

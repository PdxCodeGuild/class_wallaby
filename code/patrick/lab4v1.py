hand = []

dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A':1, 'J': 10, 'Q': 10, 'K':10}
my_sum = 0
        

while len(hand) < 3: 
    cards = input('what is your first card? ')
    
    if cards not in dict:
        print('not working')
        continue
    else:
        my_sum += dict[cards]
    hand.append(cards)
    if my_sum == 21:
        break
print(f'Current cards in your hand are {hand}.')

if my_sum == 21:
   print('Blackjack!!!')
elif my_sum < 17:
    print('hit')
elif 21 > my_sum >= 17:
    print('stay')
else: 
    print('Bust')
    
 
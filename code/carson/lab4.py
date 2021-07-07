'''
 PDX CODE
 7/2/21
 Lab 4
 Blackjack Advice
'''

cards = {

 'A' : 1,
 '1' : 1,
 '2' : 2,
 '3' : 3,
 '4' : 4,
 '5' : 5,
 '6' : 6,
 '7' : 7,
 '8' : 8,
 '9' : 9,
 '10' : 10,
 'J' : 10,
 'Q' : 10,
 'K' : 10
}
 


while True:

    a = input(f'What is you first card ? or "done" to quit. :  ')
    if a == "done":
        break
    b = input(f'What is you second card ? : ')
    c = input(f'What is you third card ? : ')

    
    a2 = cards[a]
    b2 = cards[b]
    c2 = cards[c]


    total = a2 + b2 + c2 
    
    
    if total < 17:
        print( f'HIT! ;)')
        break
    if total >= 17 and total < 21:
        print( f'STAY! :/ ')
        break
    if total == 21:
        print(f'BLACKJACK!! :)')
        break
    if total > 21:
        print(f'ALREADY BUSTED! :(') 
        break        
        
    
print(f'{total}')


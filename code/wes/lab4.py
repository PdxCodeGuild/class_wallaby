black_jack = {

'A': 1,
'2': 2,
'3': 3,
'4': 4, 
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10,

}


first_choice = input("What's your first card? ")

second_choice = input("What's your second card? ")

third_choice = input("What's your third card? ")



player_tot = black_jack[first_choice] + black_jack[second_choice] + black_jack[third_choice]

if player_tot > 21:
    print("Already Busted")
    

elif player_tot == 21:
    print("BLACKJACK")

elif player_tot >= 17:
    print("Stay")

else:
    if player_tot < 17:
            print("Hit")
    

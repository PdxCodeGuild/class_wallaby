card_table = {
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
score = 0

player_hand = [input('''\nWhat's your first card? ''' ).upper()]
player_hand.append(input('''\nWhat's your second card? ''' ).upper())
player_hand.append(input('''\nWhat's your third card? ''' ).upper())

for card in player_hand:
  if card in card_table:
    score += card_table[card]

#Checks for an ace and possiblity of changing it's value from 1 to 11. Adding the differenc, 10 if it would cause a bust
if 'A' in player_hand and score <= 11:
  score += 10

if score > 21:
  advice = 'Already Busted'
elif score == 21:
  advice = 'Blackjack!'
elif score < 17:
  advice = 'Hit'
elif score >= 17:
  advice = 'Stay'

print(f'''\n{score} {advice}''')
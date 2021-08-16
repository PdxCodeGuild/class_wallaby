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

player_hand = [input('''\nWhat's your first card? ''' ).upper()]
player_hand.append(input('''\nWhat's your second card? ''' ).upper())
player_hand.append(input('''\nWhat's your third card? ''' ).upper())
score = 0

print(player_hand)

for card in player_hand:
  if card in card_table:
    score += card_table[card]

if score > 21:
  advice = 'Already Busted'
elif score == 21:
  advice = 'Blackjack!'
elif score < 17:
  advice = 'Hit'
elif score >= 17:
  advice = 'Stay'

print(f'''\n{score} {advice}''')
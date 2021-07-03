# Lab 04: Blackjack Advice

card_values = {
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
 
print("Welcome to Blackjack Advice! Please choose 3 cards from the following: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.")
 
card_1 = input("What is your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")

card_1_value = card_values[card_1]
card_2_value = card_values[card_2]
card_3_value = card_values[card_3]

current_total_point_value = card_1_value + card_2_value + card_3_value

# convert the quantity to integer
current_total_point_value = int(current_total_point_value)


# advice
'''
* Less than 17, advise to "Hit"
* Greater than or equal to 17, but less than 21, advise to "Stay"
* Exactly 21, advise "Blackjack!"
* Over 21, advise "Already Busted"
'''

if current_total_point_value < 17:
    print(f"{current_total_point_value} Hit")

if current_total_point_value >= 17 and current_total_point_value < 21:
    print(f"{current_total_point_value} Stay")

if current_total_point_value == 21:
    print(f"{current_total_point_value} Blackjack!")

if current_total_point_value > 21:
    print(f"{current_total_point_value} Already Busted")







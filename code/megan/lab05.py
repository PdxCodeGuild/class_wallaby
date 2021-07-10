# Lab 05 - Pick 6

import random

winning_nums = []
ticket_nums = []

balance = 0

pick_6_list = []

# define pick6 function
def pick6(x): # what is x?
    while len(pick_6_list) < 6:
        pick_6_list.append(random.randint(1,99))
    return pick_6_list

print(f'{pick6(pick_6_list)}')

# define compare matches function
def num_matches(winning, ticket):
    ...



# Steps:
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
    # use enumerate?
# Add to your balance the winnings from your matches
# After the loop, print the final balance




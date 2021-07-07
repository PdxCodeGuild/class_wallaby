# Lab 05 - Pick 6

import random

winning_nums = []

# define pick6 function
def pick6():
    for i in range (0,6):
        num = random.randint(1,99)
        winning_nums.append(num)

print(winning_nums)

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
# Add to your balance the winnings from your matches
# After the loop, print the final balance




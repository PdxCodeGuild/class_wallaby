import random

pick_6_list = []

winnings_dict = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick6(list):
    while len(pick_6_list) < 6:
        pick_6_list.append(random.randint(1,99))
    return pick_6_list

#print(f'{pick6(pick_6_list)}')

def num_matches(winning, ticket):
    ...

# Generate a list of 6 random numbers representing the winning tickets
winning = pick6(pick_6_list)

# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:
for i in range(1, 100000):
    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6(pick_6_list)
    # Subtract 2 from your balance (you bought a ticket)
    balance =- 2
    # Find how many numbers match
    matches = num_matches(winning, ticket)
    # Add to your balance the winnings from your matches
    if matches > 0:
        balance += winnings_dict[matches]
    
# After the loop, print the final balance
print(balance)









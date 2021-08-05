import random

winnings_dict = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick6():
    pick_6_list = []
    while len(pick_6_list) < 6:
        pick_6_list.append(random.randint(1,99))
    return pick_6_list
# print(pick6())

def winning_ticket():
    winning_nums = []
    while len(winning_nums) < 6:
        winning_nums.append(random.randint(1,99))
    return winning_nums
# print(winning_ticket())

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches
# print(num_matches())

# 1. Generate a list of 6 random numbers representing the winning tickets
winning = winning_ticket()
# print(winning)

# 2. Start your balance at 0
balance = 0

# 3. Loop 100,000 times, for each loop:
for i in range (1, 100000): # test: (1, 6)
    # 4. Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
    # print(ticket)
    # 5. Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    # 6. Find how many numbers match
    matches = num_matches(winning, ticket)
    # print(matches)
    # 7. Add to your balance the winnings from your matches
    if matches > 0:
        balance += winnings_dict[matches]
    
# 8. After the loop, print the final balance

print(balance)

# Version 2
# ROI = (earnings - expenses) / expenses

earnings = 0
expenses = 0

# def roi(earnings, expenses)
    # earnings = += winnings_dict[matches]
    # expenses = ...



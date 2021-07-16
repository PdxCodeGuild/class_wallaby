import random

balance = 0
earnings = 0
expenses = 0

winnings_dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick6():
    """return a list of 6 random numbers from 1-99"""
    pick_6_list = []
    while len(pick_6_list) < 6:
        pick_6_list.append(random.randint(1,99))
    return pick_6_list

def winning_ticket():
    winning_nums = []
    while len(winning_nums) < 6:
        winning_nums.append(random.randint(1,99))
    return winning_nums

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

winning = winning_ticket()

for i in range (100000): 
    matches = 0
    ticket = pick6()
    balance -= 2
    expenses += 2
    earnings += winnings_dict[matches]
    matches = num_matches(winning, ticket)
    if matches > 0:
        balance += winnings_dict[matches]

roi = (earnings - expenses)/expenses 

print(f'After 100,000 tries, your balance is ${balance}.')
print(f'''
Earnings: ${earnings}
Expenses: ${expenses}
Return on investment (ROI): {roi}.
''')

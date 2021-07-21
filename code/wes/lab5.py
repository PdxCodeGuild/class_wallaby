import random


matches = {
    0: 0,
    1: 4,
    2: 7,
    3: 100, 
    4: 50000,
    5: 1000000,
    6: 25000000
}

digits = [*range(1, 100)]
random_digit = random.choice(digits)


user_balance = 0
ticket_cost = 2


winning_num = []

def pick6():
    winning_num = []
    for i in range(6):
        random_digit = random.choice(digits)

        winning_num.append(random_digit)
    return(winning_num)


winning_ticket = pick6()
user_ticket = pick6()



def num_matches(winning, ticket):
    tot_matches = 0

    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            tot_matches += 1
    return tot_matches

"""    
def scores(matches, ticket_cost):
    balance = -ticket_cost
"""
user_balance = 0
counter = 0

for _ in range(100000):
        
        user_ticket = pick6()
        user_balance -= 2

        tot_matches = num_matches(winning_ticket, user_ticket)
        user_balance += matches[tot_matches]


print(user_balance)



#print(f"You had {user_balance} match worth ${user_balance * 4}")



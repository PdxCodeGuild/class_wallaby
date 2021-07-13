import random
#------------------------------------------------------------#
def pick_6():
#------------------------------------------------------------#
    return [random.randint(1, 99) for i in range(6)]
def num_matches(winning, ticket):
    matches = 0
    for t in ticket:
        if t in winning:
            matches += 1
    return matches
#------------------------------------------------------------#
prices = [0, 4, 7, 100, 50000, 1000000, 25000000]
purse = 100000
#------------------------------------------------------------#
for i in range(100000):
    ticket = pick_6()
    winning = pick_6()
    matches = num_matches(winning, ticket)
    purse -= 2
#------------------------------------------------------------#
    if matches > 0:
        #print("Matched ", matches, "price money", prices[matches])
        purse += prices[matches]
    if purse == 0:
        print("ran out of money at turn", i)
#------------------------------------------------------------#
print("--------------------------------------------#")
print("final balance: ", purse)
print("------------------------------------#")
earnings = purse - 100000
expenses = 2 * i
print("ROI: ", (earnings - expenses) / expenses)
print("--------------------------------------------#")
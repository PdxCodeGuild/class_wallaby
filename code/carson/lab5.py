import random


ticket = []

winner = []

for i in range(0,6):
    n = random.randint(1,99)
    winner.append(n)

for i in range(0,6):
    n = random.randint(1,99)
    ticket.append(n)

'''total = winner - ticket''' # compare both list and return matches 

payout = {
'ticket' : 2,
 '1' : 4,
 '2' : 7,
 '3' : 100,
 '4' : 50000,
 '5' : 1000000,
 '6' : 25000000,
}

print(total) #Print matches from total list.
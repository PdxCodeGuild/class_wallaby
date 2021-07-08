import random


ticket = []

winner = []
i = 1
while i <= 100000: #Loop function
    
    
    
    for i in range(0,6):
        n = random.randint(1,99)
        winner.append(n)

    for i in range(0,6):
        n = random.randint(1,99)
        ticket.append(n)


total = set(winner) & set(ticket) # compare both list and return matches 



payout = {
 1 : 4,
 2 : 7,
 3 : 100,
 4 : 50000,
 5 : 1000000,
 6 : 25000000
}

x = len(total)

x = payout.get(x)

print(f' Congratulations you won ${x} !! :)' )

print(f'Ticket Numbers: {ticket}')

print(f'Winning Numbers: {winner}')
#print(f'You Won ${x2} ')

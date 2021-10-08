import random

def pick6():
  num = []
  while len(num) < 6:
    num.append(random.randint(1, 99))
    num =list(set(num))
  return num

def matches(winner, ticket):
  match = 0
  for i in range(len(winner)):
    if winner[i] == ticket[i]:
      match += 1
  return match

#-------------------------------------------------------------------#
balance = 0
ticket_cost = 2
ticket = []
winner = []

payout = {
0 : 0,
1 : 4,
2 : 7,
3 : 100,
4 : 50000,
5 : 1000000,
6 : 25000000
}

earnings = 0
expenses = 0
 

winner = pick6()

i = 1
for i in range(100_000): #Loop function
  ticket = pick6()
  total = matches(winner,ticket)  
  x = payout.get(total)  
  balance -= ticket_cost
  balance += x  
  earnings += x
  expenses += ticket_cost

print((earnings - expenses)/expenses)
#print(balance)
#print(total)
print(f' Congratulations you won ${balance} !! :)' )
#print(f'Ticket Numbers: {ticket}')
#print(f'Winning Numbers: {winner}')


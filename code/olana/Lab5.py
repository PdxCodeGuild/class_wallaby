import random 
total = 0
amount = []

def pick6():
  return(random.sample(range(0, 99), 6,))
winning_ticket = pick6()
print(f"The winning_ticket is: {winning_ticket}")
for _ in range(100000):
    random_ticket = pick6()
    print(random_ticket)
    compare_tickets = [True if i == j else False for i,j in zip(random_ticket, winning_ticket)]
    match_count = sum(compare_tickets)
    if match_count == 0:
        amount =-2
        total = total + amount
    if match_count == 1:
        amount =+4
        total = total + amount
    if match_count == 2:
        amount =+7
        total = total + amount
    if match_count == 3:
        amount =+100
        total = total + amount
    if match_count == 4:
        amount =+50000
        total = total + amount
    if match_count == 5:
        amount =+1000000
    if match_count == 6:
        amount =+ 250000000
       
print(compare_tickets)
print(match_count)
print(total)
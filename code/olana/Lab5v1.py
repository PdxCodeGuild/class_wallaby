#1. Generate a list of 6 random numbers representing the winning tickets
#2. Start your balance at 0
#2. Loop 100,000 times, for each loop:
#3. Generate a list of 6 random numbers representing the ticket
#4. Subtract 2 from your balance (you bought a ticket)
#5. Find how many numbers match 
#6. Add to your balance the winnings from your matches
#7. After the loop, print the final balance


#https://pynative.com/python-random-randrange/
#https://www.kite.com/python/docs/collections.Counter





#1. Generate a list of 6 random numbers representing the winning ticket
#print("Winning Ticket: ", random.sample(range(0, 99), 6))

import random 

def pick6():
  return(random.sample(range(0, 99), 6))
computer_ticket = pick6()
a = enumerate(computer_ticket)
print(list(a))
#print(winning_ticket)

#3. Generate a list of 6 random numbers representing the ticket
#print("My Ticket: ", random.sample(range(0, 99), 6))

def lottery_ticket():
  return(random.sample(range(0, 99), 6))  
my_ticket = lottery_ticket()
b = enumerate(my_ticket)
print(list(b))
#print(my_ticket)


#def num_matches():
    #return 

if a == b:
    print("match")
else:
    print("no match")



#1. Generate a list of 6 random numbers representing the winning tickets
#2. Start your balance at 0
#2. Loop 100,000 times, for each loop:
#3. Generate a list of 6 random numbers representing the ticket
#4. Subtract 2 from your balance (you bought a ticket)
#5. Find how many numbers match 
#6. Add to your balance the winnings from your matches
#7. After the loop, print the final balance

#Citations:
#https://pynative.com/python-random-randrange/
#https://www.kite.com/python/docs/collections.Counter
#https://www.w3schools.com/python/default.asp
#https://stackoverflow.com/questions/21771964/list-index-comparison-in-python
#https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/
#https://www.codespeedy.com/python-check-if-all-the-elements-in-a-list-are-equal/
#https://stackoverflow.com/questions/38035317/comparing-same-index-in-2-lists


#1. Generate a list of 6 random numbers representing the winning ticket
#print("Winning Ticket: ", random.sample(range(0, 99), 6))

import random 

def pick6():
  return(random.sample(range(0, 99), 6))
computer_ticket = pick6()
a = enumerate(computer_ticket)
print(list(a))
#print(computer_ticket)

def lottery_ticket():
  return(random.sample(range(0, 99), 6))  
my_ticket = lottery_ticket()
b = enumerate(my_ticket)
print(list(b))
#print(my_ticket)

winning_ticket = [True if i == j else False for i,j in zip(my_ticket, computer_ticket)]
print(winning_ticket)

'''
winning_ticket = []
counter = 0

for num in my_ticket:  
    if num in computer_ticket:
        counter +=1
print(str(counter) + " matched")
'''







        


#computer_ticket,my_ticket = [],[]
#print[index for index,(e1,e2) in enumerate(zip(computer_ticket, my_ticket)) if e1 == e2]



#for i, nums in enumerate(computer_ticket):
    #print(f"{i}: {computer_ticket}")



    
#print(computer_ticket)
#a = enumerate(computer_ticket)
#print(list(a))
#print(winning_ticket)

#3. Generate a list of 6 random numbers representing the ticket
#print("My Ticket: ", random.sample(range(0, 99), 6))
'''
def lottery_ticket():
  return(random.sample(range(0, 99), 6))  
my_ticket = lottery_ticket()
print(my_ticket)
b = enumerate(my_ticket)
print(list(b))
print(my_ticket)
'''



    



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
#https://www.kite.com/python/answers/how-to-count-the-number-of-true-booleans-in-a-list-in-python


#1. Generate a list of 6 random numbers representing the winning ticket


import random 

def pick6():
  return(random.sample(range(0, 99), 6,))
computer_ticket = pick6()
print(computer_ticket)

#3. Generate a list of 6 random numbers representing the ticket
def lottery_ticket():
  return(random.sample(range(0, 99), 6))  
my_ticket = lottery_ticket()
print(my_ticket)



#5. Find how many numbers match 
winning_ticket = [True if i == j else False for i,j in zip(my_ticket, computer_ticket)]
print(winning_ticket)

match_count = sum(winning_ticket)
print(match_count)

#2. Start your balance at 0 and loop 100,000 times


#6. Add to your balance the winnings from your matches
counter = 0
counter_list = []


if match_count == 0:
    counter =-2
    counter_list.append(counter)
elif match_count == 1:
    counter =+4
    counter_list.append(counter)
elif match_count == 2:
    counter =+7
    counter_list.append(counter)
elif match_count == 3:
    counter =+100
    counter_list.append(counter)
elif match_count == 4:
    counter =+50000
    counter_list.append(counter)
elif match_count == 5:
    counter =+1000000
    counter_list.append(counter)
elif match_count == 6:
    counter =+25000000
    counter_list.append(counter)
print(counter)
print(counter_list)
#balance = sum(counter_list)

    



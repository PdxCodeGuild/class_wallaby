import random

def pick6():
    picks = [] # list 
    while len(picks) < 6:
        picks.append(random.randrange(1, 100)) #randrange includes step and non inclusive, randint does not include step and is   
    return picks
def winning():
    pick = []
    while len(pick) < 6:
        pick.append(random.randrange(0, 100))
    return pick


def money(matches):
    dollars = 0
    if matches == 1:
        dollars += 4
    elif matches == 2:
        dollars += 7
    elif matches == 3:
        dollars += 100
    elif matches == 4:
        dollars += 50000
    elif matches == 5:
        dollars += 1000000
    elif matches == 6:
        dollars += 25000000
    return dollars 
balance = 0

for i in range(100000):
    balance -= 2
    match_1 = 0
    attempt = pick6()
    win = winning()  
    for i in range(len(attempt)):
       if win[i] == attempt[i]:
           match_1 += 1
    balance += money(match_1)

print(f'Your winnings over losses comes to ${balance}')
            

    
    
    
        




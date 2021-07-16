import random

def pick6():
	"""return a list of 6 random numbers from 1 - 99"""
	ticket = []
	while len(ticket) < 6:
		ticket.append(random.choice(range(1, 100)))
		# ticket = list(set(ticket)) # this didn't work :(
	return ticket

def num_matches(winning_ticket, ticket):
	"""return number of matches between ticket and winning ticket"""
	matches = 0
	for i in range(len(winning_ticket)):
		if ticket[i] == winning_ticket[i]:
			matches += 1
	return matches

matches_to_dollars = {
	0: 0,
	1: 4,
	2: 7,
	3: 100,
	4: 50_000,
	5: 1_000_000,
	6: 25_000_000
}

# Generate a list of 6 random numbers representing the winning ticket
winning_ticket = pick6()

# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:
print(winning_ticket)
for _ in range(100_000):
	# Generate a list of 6 random numbers representing the ticket
	ticket = pick6()
	# print(ticket)
	# Subtract 2 from your balance (you bought a ticket)
	balance -= 2
	# Find how many numbers match
	matches = num_matches(winning_ticket, ticket)
	if matches > 3:
		print('hit')
	# print(matches)
	# Add to your balance the winnings from your matches
	balance += matches_to_dollars[matches]

# After the loop, print the final balance
print(balance)
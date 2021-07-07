import random

balance = 0 # why can't this variable be referenced within the def?
ticket_cost = 2

matches_dict = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
  }

# **** F U N C T I O N S ****
def pick6():
  six_list = []
  while len(six_list) < 6:
    six_list.append(random.randint(1, 99))
  return six_list

def num_matches(winning, ticket):
  matches = 0
  for idx in range(len(winning)):
    if winning[idx] == ticket[idx]:
      matches += 1
  return matches

def scorekeeper(matches, ticket_cost):
  balance = -ticket_cost

  if matches > 0:
    balance += matches_dict[matches]
  return balance

def play(num_of_tickets):
  winning = pick6()
  balance = 0
  for i in range(num_of_tickets):
    balance += scorekeeper(num_matches(winning, pick6()), ticket_cost)
  print(f'''Balance: {'-' if balance < 0 else ''}${abs(balance)}''')
  return balance, num_of_tickets

def roi(balance, num_of_tickets):
  expenses = ticket_cost * num_of_tickets
  pre_expense_bal = balance + expenses
  winnings = pre_expense_bal - expenses
  roi = winnings / expenses * 100
  print(f'''
    \nROI: {roi}%
    Earnings: {winnings}
    Expenses: {expenses}
  ''')
  return roi, winnings, expenses

balance, num_of_tickets = play(100000)

roi(balance, num_of_tickets)

# **** T E S T S ****
def test_pick6():
  pick6_list = pick6()
  # A list should be returned
  assert type(pick6_list) == list
  for num in pick6_list:
    # Each value in list should be int
    assert type(num) == int
    # Each int should be 1-99
    assert num >= 1 and num <= 99
  # list length should be 6
  assert len(pick6_list) == 6

# test for proper positional matches
def test_num_matches():
  assert num_matches([1, 2, 3, 4, 5, 6], [5, 1, 3, 8, 2, 6]) == 2
  assert num_matches([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]) == 0
  assert num_matches([1, 2, 3, 4, 5, 6], [5, 6, 8, 4, 9, 10]) == 1

# test matches 0-6 for correct return
def test_scorekeeper():
  assert scorekeeper(0, ticket_cost) == -ticket_cost
  assert scorekeeper(1, ticket_cost) == matches_dict[1]-ticket_cost
  assert scorekeeper(2, ticket_cost) == matches_dict[2]-ticket_cost
  assert scorekeeper(3, ticket_cost) == matches_dict[3]-ticket_cost
  assert scorekeeper(4, ticket_cost) == matches_dict[4]-ticket_cost
  assert scorekeeper(5, ticket_cost) == matches_dict[5]-ticket_cost
  assert scorekeeper(6, ticket_cost) == matches_dict[6]-ticket_cost

def test_play():
  assert play(1) == 2 or -2

def test_roi():
  assert roi(2, 1) == (100.0, 2, 2)
  assert roi(-2, 1) == (-100.0, -2, 2)
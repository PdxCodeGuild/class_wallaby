class ATM:
    def __init__(self, balance, interest_rate):
        self.current_balance=balance
        self.interest_rate=interest_rate
        self.transactions = []

    def check_balance(self):
		#return the account balance
        return self.current_balance 
	
    def deposit(self, amount):
		#deposit a given amount into account
	    self.current_balance += amount
        self.transactions.append(f'User Deposited: {amount}')

    def check_withdrawal(self, amount):
		#return True if account has enough funds to withdraw given amount
        if amount <= self.current_balance:
            return True
        else:
            amount > self.current_balance
            return False

    def withdraw(self, amount):
		#withdraw given amount from account and return that amount
        if self.check_withdrawal(amount)== True:
            self.current_balance - amount
            self.transactions.append(f'User Withdraw: {amount}')
            return self.current_balance
            
    def calc_interest(self):
		#calculate and return interest gained on account
        balance * self.interest_rate
        return amount
    
    def print_transaction(self):
        return self.transactions
    

atm = ATM(0,0.1) # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'User Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    
    elif command == 'transaction':
        print(atm.print_transaction())

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')



balance_1 = 0 #confused as to why this is not gloabal. Used global for v1.1, then I figured out that I needed to add amount to interest_calc below in order to insert calc_interest(self,
class ATM: 
    def __init__(self):
        self.balance = 0 
        print('Welcome to the ATM')
        print('''Please chose from the following:

1. Balance
2. Deposit
3. Withdraw
4. Interest          
 ''')
    def check_balance(self):
        
        return self.balance
    
    # def check_balance(self):
    #     global balance_1 
    #     return balance_1
    
    def deposit(self, amount):
        self.balance += amount
        return amount 
    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        elif amount <= self.balance:
            return True
    def withdraw(self, amount):
        self.balance -=  amount
        return amount
    
    def calc_interest(self, amount): #should this be happening at _init_? Everytime this is called, interest is calculated and added to balance. 
        amount = round((self.balance *.10), 2)
        return amount

    
atm = ATM() # create an instance of our class
while True:
    
    command = input('Enter a command: ').lower()
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        try:
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
        except:
            print("Not a valid entry, returning to the main menu.")
            continue
    elif command == 'withdraw':
        
        try:
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')

        except:
            print('Not a valid entry, returning to the main menu.')
    elif command == 'interest':
        amount = atm.calc_interest(amount) # Added amount in order to recieve two arguments
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
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
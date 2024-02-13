class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_balance = 500
        self.max_balance = 100000
        
    def depossite(self,amount):
        self.balance += amount
        print(f'After depossite your current Balance is {self.balance}')
    
    def cheak_balance(self):
        print(f'Your current balance is {self.balance}')
        
    def withdraw(self,amount):
        if amount < self.min_balance:
            print('You cannot withdraw this amount , increase your amount')
        elif amount > self.max_balance:
            print('You cannot withdraw this amount , decrease your amount')
        elif amount > self.balance:
            print('You have insufficient balance')
        else:
            self.balance -= amount
            print(f"After withdraw your current amount is {self.balance}")
            
brac = Bank(12000)
brac.cheak_balance()

brac.depossite(3000)
brac.cheak_balance()

brac.withdraw(70)
brac.cheak_balance()
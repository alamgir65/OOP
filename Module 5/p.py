class Bank:
    def __init__(self,buyer):
        self.buyer = buyer
        self.min_withdraw = 500
        self.max_withdraw = 100000
        self.balance = 0
        
    def depossite(self,amount):
        self.balance += amount
        print(f'After depossite your new balance is {self.balance}')
    
    def cheak_balance(self):
        print(f"Your Current balance is {self.balance}")
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f"You cannot withdraw minimum {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"You cannot withdraw maximum {self.max_withdraw}")
        elif amount > self.balance:
            print('You have insufficient balance')
        else:
            self.balance -= amount 
            print(f'After Withdraw your Current balance is {self.balance}')
            
asia = Bank('Asia Bank')
asia.depossite(5200)
asia.cheak_balance()

asia.withdraw(2000)
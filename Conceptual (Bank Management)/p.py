from abc import ABC, abstractmethod

class Account(ABC):
    accounts = []

    def __init__(self, name, acc_number, password, type_) -> None:
        super().__init__()
        self.name = name
        self.acc_number = acc_number
        self.password = password
        self.balance = 0
        self.type = type_
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print('Deposit not allowed Negative balance')

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f'Your {amount} tk withdraw successfully, New Balance : {self.balance}')
        else:
            print('Invalid balance')

    def changeInfo(self, name, password=None):
        self.name = name
        if password:
            self.password = password

    @abstractmethod
    def showInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, acc_number, password, interest_rate) -> None:
        super().__init__(name, acc_number, password, 'savings')
        self.interest_rate = interest_rate

    def showInfo(self):
        print(f'Name : {self.name}\n Balance : {self.balance}\n Account Type : {self.type} \n Account Number : {self.acc_number}')

    def applyInterest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f'Interest is applied tk : {interest}')
        self.deposit(interest)

class SpecialAccount(Account):
    def __init__(self, name, acc_number, password, limit) -> None:
        super().__init__(name, acc_number, password, 'special')
        self.limit = limit

    def withdraw(self, amount):
        if 0 <= amount <= self.limit + self.balance:
            self.balance -= amount
        else:
            print('Invalid amount')

    def showInfo(self):
        print(f'Name : {self.name}\n Balance : {self.balance}\n Account Type : {self.type} \n Account Number : {self.acc_number}')

current_user = None

def main():
    while True:
        global current_user
        if current_user is None:
            print('--No User Login--')
            op = input('Choose Option Login or Registration (L/R)')

            if op == 'R':
                option = input('Choose Savings or Special account (sv/sp) :')
                if option == 'sv':
                    name = input('Enter your name : ')
                    accNum = input('Enter your Account Number : ')
                    interest_rate = float(input('Enter your Interest Rate : '))  # Convert to float
                    password = input('Enter your password : ')
                    current_user = SavingsAccount(name, accNum, password, interest_rate)
                else:
                    name = input('Enter your name : ')
                    accNum = input('Enter your Account Number : ')
                    limit = float(input('Enter your limit : '))  # Convert to float
                    password = input('Enter your password : ')
                    current_user = SpecialAccount(name, accNum, password, limit)

            else:
                accNum = input('Enter Your Account Number : ')
                password = input('Enter Your Password : ')

                for account in Account.accounts:
                    if account.acc_number == accNum and account.password == password:
                        current_user = account
                        break
        else:
            print(f'\n Welcome {current_user.name}')

            if current_user.type == 'savings':

                print('Option 1 : Deposit Balance')
                print('Option 2 : Withdraw')
                print('Option 3 : Change Info')
                print('Option 4 : Show Info')
                print('Option 5 : Apply Interest')
                print('Option 6 : Logout')

                op = int(input('Choose your option : '))  # Convert to int

                if op == 1:
                    amount = float(input('Enter Your deposit Amount : '))  # Convert to float
                    current_user.deposit(amount)
                elif op == 2:
                    amount = float(input('Enter Your Withdraw Amount : '))  # Convert to float
                    current_user.withdraw(amount)
                elif op == 3:
                    print('Option 1 : Change Only Name : ')
                    print('Option 2 : Change Name and Password : ')

                    ch = int(input('Choose option : '))  # Convert to int
                    if ch == 1:
                        name = input('Enter Your Name : ')
                        current_user.changeInfo(name)
                    elif ch == 2:
                        name = input('Enter Your Name : ')
                        password = input('Enter Your Password : ')
                        current_user.changeInfo(name, password)
                    else:
                        print('Invalid Option')
                elif op == 4:
                    current_user.showInfo()
                elif op == 5:
                    current_user.applyInterest()
                elif op == 6:
                    current_user = None
                else:
                    print('Invalid Option')

            else:
                print('Option 1 : Deposit Balance')
                print('Option 2 : Withdraw')
                print('Option 3 : Change Info')
                print('Option 4 : Show Info')
                print('Option 5 : Logout')

                op = int(input('Choose your option : '))  # Convert to int

                if op == 1:
                    amount = float(input('Enter Your deposit Amount : '))  # Convert to float
                    current_user.deposit(amount)
                elif op == 2:
                    amount = float(input('Enter Your Withdraw Amount : '))  # Convert to float
                    current_user.withdraw(amount)
                elif op == 3:
                    print('Option 1 : Change Only Name : ')
                    print('Option 2 : Change Name and Password : ')

                    ch = int(input('Choose option : '))  # Convert to int
                    if ch == 1:
                        name = input('Enter Your Name : ')
                        current_user.changeInfo(name)
                    elif ch == 2:
                        name = input('Enter Your Name : ')
                        password = input('Enter Your Password : ')
                        current_user.changeInfo(name, password)
                    else:
                        print('Invalid Option')
                elif op == 4:
                    current_user.showInfo()
                elif op == 5:
                    current_user = None
                else:
                   print('Invalid Option')
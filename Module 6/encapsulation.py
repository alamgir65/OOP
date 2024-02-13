# kono akta value ke private korar jonno double underscore use kora lage
# such as --> __balance
#protected --> _balnce
#privat --> __balance
#public --> balance
class Bank:
    def __init__(self,owner,initial_balance) -> None:
        self.owner = owner
        self.__balance = initial_balance
        self.pin = '23@525'
        
    def deposit(self,amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount,PIN):
        if PIN != self.pin:
            print('Your pin is wrong')
        else:
            if amount > self.__balance:
                print('You have insufficient balance')
            else:
                self.__balance -= amount
                print(f'You rechive {amount} tk , and after withdraw Your balance is {self.__balance}')
                
# my_bank.balance = 2000 aikhane amra class er bahire theke access korte pari
#but jodi amra encapsulation use kori tahole eita r bahir theke access kora jabe nah
# print(my_bank.__balance) aybabe access kora jai nah

my_bank = Bank('Alamgir',10000)
my_bank.deposit(5000)
print(my_bank.get_balance())

my_bank.withdraw(4000,'23@525')
my_bank.withdraw(4000,'23@524')
my_bank.withdraw(42000,'23@525')
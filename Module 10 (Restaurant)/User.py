from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,email,phone,address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        super().__init__()

class Customer(User):
    def __init__(self, name,money,email,phone,address) -> None:
        self.money = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name,email,phone,address)
    
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order = order
    
    def placed_order(self,order):
        self.order = order
        self.due_amount += order.bill
        print(f"{self.name} placed an order with bill: {order.bill}")
    
    def pay_for_order(self):
        pass
    
    def give_tips(self,amount):
        pass
    
    def write_review(self,stars):
        pass

class Employee(User):
    def __init__(self, name, email, phone, address,salary,starting_date) -> None:
        self.starting_date = starting_date
        self.salary = salary
        self.due = salary
        super().__init__(name, email, phone, address)
        
    def rechive_salary(self):
        self.due =0
    

class Chef(Employee):
    def __init__(self, name, email, phone, address, salary, starting_date,cooking_item) -> None:
        super().__init__(name, email, phone, address, salary, starting_date)
        self.cooking_item = cooking_item
    

class Server(Employee):
    def __init__(self, name, email, phone, address, salary, starting_date) -> None:
        super().__init__(name, email, phone, address, salary, starting_date)
        self.earning_tips = 0
    
    def take_order(self,order):
        pass
    
    def transfer_order(self,order):
        pass
    
    def serve_food(self,order):
        pass
    
    def rechive_tips(self,amount):
        self.earning_tips += amount

class Manager(Employee):
    def __init__(self, name, email, phone, address, salary, starting_date) -> None:
        super().__init__(name, email, phone, address, salary, starting_date)
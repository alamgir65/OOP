class Restuarant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.rent = rent
        self.manager = None
        self.server = None
        self.menu = menu
        self.revenue = 0
        self.profit = 0
        self.balance = 0
        self.expense = 0
    def add_emlpoyee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'manager':
            self.manager = employee
        elif employee_type == 'server':
            self.server = employee
    
    def add_order(self,order):
        self.orders.append(order)
    
    def rechive_payment(self,amount,order,customer):
        print(f"Your Total bill : {order.bill}")
        if amount >= order.bill :
            self.balance += order.bill
            self.revenue += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print("Your money is not enough,pay more")
    
    def pay_expense(self,amount,description):
        if amount <= self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"Expense {amount} for {description}")
        else:
            print(f"Not enough money for {amount}")
    
    def pay_salary(self,employee):
        print(f"paying salary for employee name: {employee.name} and Salary: {employee.salary}")
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.rechive_salary()
            
    def show_employee(self):
        print("This is Our all Employee")
        
        if self.chef is not None:
            print(f"Chef Name : {self.chef.name} and Email: {self.chef.email}")
        if self.manager is not None:
            print(f'Manager Name : {self.manager.name} and Email: {self.manager.email} ')
        if self.server is not None:
            print(f'Server Name : {self.server.name} and Email: {self.server.name}')
            
    
    
            
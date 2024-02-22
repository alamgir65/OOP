from Menu import Pizza,Burger,Drink,Menu
from Restuarantclass import Restuarant
from User import Chef,Manager,Server,Customer
from Order import Order
def main():
    
    #Add menu item
    pizza_1 = Pizza('Shutki Pizza',600,'Large',['Shutki','onion'])
    pizza_2 = Pizza('Alur Pizza',800,'Medium',['potato','onion'])
    pizza_3 = Pizza('Dal Pizza',1000,'Small',['Dal','onion'])
    
    menu = Menu()
    menu.add_menu_item('pizza',pizza_1)
    menu.add_menu_item('pizza',pizza_2)
    menu.add_menu_item('pizza',pizza_3)
    
    burger_1 = Burger('Beef Burger',300,'beef',['goru','oil'])
    burger_2 = Burger('Naga Burger',500,'Chiken',['goru','oil'])
    
    menu.add_menu_item('burger',burger_1)
    menu.add_menu_item('burger',burger_2)
    
    coffee = Drink('Coffee',80,False)
    coke = Drink('Coke',60,True)
    
    menu.add_menu_item('drink',coffee)
    menu.add_menu_item('drink',coke)
    
    # menu.show_menu()
    
    #add Employee
    restuarant = Restuarant('Sai Baba Restuarant',1000,menu)
    manager = Manager("Chan Mia Manager",'chan@mia.com',41765467,'chanphur',1500,'1 jan 2020')
    restuarant.add_emlpoyee('manager',manager)
    
    chef = Chef('Kala Baburchi','kala@baburchi.com',4536275,'kalaphur',1000,'02 jan 1994' ,'Everything')
    restuarant.add_emlpoyee('chef',chef)
    
    server = Server('Rohan','rohan@mim.com',64732564,'Khetar Khatti',200,'sep 12 2023')
    restuarant.add_emlpoyee('server',server)
    
    # restuarant.show_employee()
    
    # Add Customer1 and place order
    customer1  = Customer('Sakib Khan',100000,'shakib@king.com',5734536,'Banani')
    order_1 = Order(customer1,[pizza_2,coffee])
    customer1.placed_order(order_1)
    restuarant.add_order(order_1)
    
    #customer pay for order_1
    restuarant.rechive_payment(2000,order_1,customer1)
    
    print(f"Revenue and Balance After 1st customer: {restuarant.revenue} and {restuarant.balance}")
    
     # Add Customer2 and place order
    customer2  = Customer('Sakib Khan',100000,'shakib@king.com',5734536,'Banani')
    order_2 = Order(customer2,[pizza_2,coffee,burger_1,pizza_1,pizza_3])
    customer2.placed_order(order_2)
    restuarant.add_order(order_2)
    
    #customer pay for order_2
    restuarant.rechive_payment(5000,order_2,customer2)
    
    print(f"Revenue and Balance After 2nd customer: {restuarant.revenue} and {restuarant.balance}")
    
    #pay rent
    restuarant.pay_expense(restuarant.rent,'For Rent')
    print(f"After Expense for Rent, Revenue {restuarant.revenue} , Balance {restuarant.balance} and Expense {restuarant.expense}")
    
    #pay salary
    restuarant.pay_salary(chef)
    print(f"After Expense for salary, Revenue {restuarant.revenue} , Balance {restuarant.balance} and Expense {restuarant.expense}")
    
    
if __name__ == '__main__':
    main()
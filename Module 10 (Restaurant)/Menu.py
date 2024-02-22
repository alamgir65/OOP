class Food:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

class Burger(Food):
    def __init__(self, name, price,meat,ingredient) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredient = ingredient

class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drink(Food):
    def __init__(self, name, price,isCold) -> None:
        super().__init__(name, price)
        self.isCold = isCold
        

class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []
    
    def add_menu_item(self,item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drink':
            self.drinks.append(item)
    
    def remove_pizza(self,item):
        if item in self.pizzas:
            self.pizzas.remove(item)
    
    def show_menu(self):
        print("This is our Menu : \n")
        for pizza in self.pizzas:
            print(f"Name : {pizza.name} , Price : {pizza.price}")
        
        for burger in self.burgers:
            print(f"Name : {burger.name} , Price : {burger.price}")
        
        for drink in self.drinks:
            print(f"Name : {drink.name}, Price: {drink.price}")


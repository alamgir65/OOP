class Product:
    def __init__(self) -> None:
        self.stock_product = []
    
    def __repr__(self) -> None:
        for item in self.stock_product:
            print(f"Name : {item['name']} , Quantity : {item['quantity']} , Price : {item['price']} ")
    

class Shop(Product):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
    
    def add_product(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        product = {'name' : self.name , 'price' : self.price , 'quantity' : self.quantity}
        self.stock_product.append(product)
    
    def buy_product(self,p_name,p_quantity,amount):
        i = 0
        index = -1
        stock_quantity = 0
        for item in self.stock_product:
            if item['name'] == p_name:
                index = i
                stock_quantity = item['quantity']
                
            i += 1
        if index == -1:
            print(f"This {p_name} product is not available now")
        elif stock_quantity < p_quantity:
            print(f"You will take at most : {stock_quantity} quantity , more than is not available now")
        else:
            cost = self.stock_product[index]['price'] * p_quantity
            if cost > amount:
                print(f"Your money is not enough for this product, please pay more {cost-amount}")
            else:
                print(f"Congratulation! you rechive your product.Your total cost : {cost} And rechive your extra balance is : {amount-cost}")

add = Shop('Alamgir Super Shop')

add.add_product('Alu',55,100)
add.add_product('kodhu',20,30)
add.add_product('Mula',15,60)
add.add_product('Dim',10,100)
add.add_product('Fish',200,10)

add.buy_product('Alu',10,2000)
add.buy_product('Dim',200,2000)
add.buy_product('Fish',9,200)
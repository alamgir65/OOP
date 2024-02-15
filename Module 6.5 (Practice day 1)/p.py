class Product:
    stock_product = []
    def __init__(self) -> None:
        pass
    
class Shop(Product):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
        
    def add_to_cart(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.qunatity = quantity
        product = {'name' : self.name , 'price' : self.price,'quantity' : self.qunatity}
        
        self.stock_product.append(product)
        
    def buy_product(self,p_name,p_quantity,amount):
        i = 0
        index = -1
        for item in self.stock_product:
            if item['name'] == p_name:
                index = i
            i += 1
        
        if(index == -1):
            print("Sorry!! This Product is not Available now")
        else:
            cost = self.stock_product[index]['price']*p_quantity
            if self.stock_product[index]['quantity'] < p_quantity:
                print(f"Our this product is not enough available as you want you take at most {index['quantity']}\n")
            elif amount < cost:
                print(f"Your money is not enough pay more {cost-amount}")
            else:
                print(f"Your your product and rechive extra balance {amount - cost}")

shop = Shop('Ma Super Shop')
shop.add_to_cart('Rice',70,200)
shop.add_to_cart('Fish',200,20)
shop.add_to_cart('Potato',40,200)
shop.add_to_cart('Mango',100,50)
shop.add_to_cart('Rice',70,200)

shop.buy_product('Rice',2,1000)

# s_product = int(input("Enter your Product number in your Shop : "))
# for i in range(s_product):
#     item = (input("Enter Product Name : "))
#     quantity = int(input("Enter product Quantity : "))
#     price = int(input("Enter product Price : "))
#     shop.add_to_cart(item,price,quantity)
    
# need = int(input("Enter number of item : "))
# for i in range(need):
#     item = (input("Enter Product Name : "))
#     quantity = int(input("Enter product Quantity : "))
#     amount = int(input("Enter product total amount : "))
#     shop.buy_product(item,quantity,amount)

class Shopping:
    def __init__(self,customer):
        self.customer = customer
        self.total_amount = 0
        self.cart = []
    
    def remove_from_cart(self,item):
        for it in self.cart:
            for j in it:
                if j == item:
                    tmp = it['price'] * it['quantity']
                    self.total_amount -= tmp
                    break
        print(f'After your product remove your balance is {self.total_amount}')
    def add_to_cart(self,item,price,quantity):
        product = {'item ': item,'price': price ,'quantity': quantity}
        self.cart.append(product)
        self.total_amount += price * quantity
    
    def cheak_out(self,amount):
        print(self.cart)
        print(f'Your total amount is {self.total_amount}')
        if amount < self.total_amount:
            print(f'Please give more than {self.total_amount - amount}')
        else:
            print(f"Take your extra money : {amount - self.total_amount}")
            
alamgir = Shopping('Alamgir')
alamgir.add_to_cart('alu',50,5)
alamgir.add_to_cart('dim',10,8)
alamgir.add_to_cart('Rice',70,15)

# alamgir.cheak_out(1500)
# alamgir.cheak_out(1000)

alamgir.remove_from_cart('dim')

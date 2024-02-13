class Shop:
    def __init__(self,bayer):
        self.bayer = bayer
        self.cart = [] # here this cart is instance attributes, aikhane sudu akjon bayer er item gula dekhte parbo
        
    def add_to_cart(self,item):
        self.cart.append(item)
    
mehzabeen = Shop('Meh ja been')
mehzabeen.add_to_cart('Phone')
mehzabeen.add_to_cart('Churi')
print(mehzabeen.cart)

nisho = Shop('Afran nisho')
nisho.add_to_cart('Smart Watch')
nisho.add_to_cart('Cap')
print(nisho.cart)


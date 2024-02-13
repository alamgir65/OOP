class Shop:
    cart = [] #this is class attiribute aikhane kono kichu add korle sob e access hobe
    def __init__(self,name):
        self.name = name
        
    def add_to_cart(self,item):
        self.cart.append(item)

mehzabeen = Shop('Meh Jabeeen')
mehzabeen.add_to_cart('Shoes')
mehzabeen.add_to_cart('Phone')
mehzabeen.add_to_cart('Churi')
print(mehzabeen.cart)

Nisho = Shop('Afran nisho')
Nisho.add_to_cart('Watch')
Nisho.add_to_cart('Chigarate')

print(Nisho.cart)
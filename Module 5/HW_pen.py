class Pen:
    def __init__(self,Brand,Price,Colour):
        self.Brand = Brand
        self.Price = Price
        self.Colour = Colour
        
Matador = Pen('Metador ',10,'Blue')
Alpha = Pen('Alpha boss',15,'Black')
pin_point = Pen('Pen Point ',20,'Red')

print(Matador.Brand,Matador.Colour,Matador.Price,sep=' --> ')
print(Alpha.Brand,Alpha.Colour,Alpha.Price)
print(pin_point.Brand,pin_point.Colour,pin_point.Price)
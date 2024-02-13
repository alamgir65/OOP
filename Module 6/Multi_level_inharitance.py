class Vehical:
    def __init__(self,name,price,colour) -> None:
        self.name = name
        self.price = price
        self.colour = colour
    
    def __repr__(self) -> str:
        return f" This is Vehical Segment --> \nCar name {self.name} , colour {self.colour} and price is {self.price}\n"
    
class Bus(Vehical):
    def __init__(self, name, price, colour,seat) -> None:
        self.seat = seat
        super().__init__(name, price, colour)
        
    def __repr__(self) -> str:
        print(f"This is Bus Segment -->\n Your car name is  {self.name }, Price : {self.price} , Colour : {self.colour} and Seat : {self.seat}\n")
        return super().__repr__()
    
class AcBus(Bus):
    def __init__(self, name, price, colour, seat,tempareture) -> None:
        self.tempareture = tempareture
        super().__init__(name, price, colour, seat)
        
    def __repr__(self) -> str:
        print(f"This is Acbus Segment -->\n Your car name is  {self.name }, Price : {self.price} , Colour : {self.colour} and Seat : {self.seat} , Tempareture : {self.tempareture}\n")
        return super().__repr__()
    
my_bus = AcBus('Lal Shabuj',502891225,'Red and Blue',22, '25 Celcius')
print(my_bus)
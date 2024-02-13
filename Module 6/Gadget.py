
class Laptop:
    def __init__(self,brand,price,memory,colour):
        self.brand = brand
        self.price = price
        self.memory = memory
        self.colour = colour
    
    def cheak(self):
        return f'Your Laptop is running now'
    
class Phone:
    def __init__(self,brand,price,colour,dual_sim):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.dual_sim = dual_sim
        
    def phone_call(self,number):
        return f'Your call is going to {number}'
    
class Camera:
    def __init__(self,brand,price,colour,pixel):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.pixel = pixel
        
    def change_lens(self):
        pass
# base classs , parent class , common attributes + functionality class
# kichu jinish jodi amader sob class a same e thake tahole amra base class create korbo 
# common class er jinish gular base class createt koratai inharitance

#jegula uncommon thakbe segulake,, derived class, uncommon class, uncommon attributes + functionality bole


class Gadget:
    def __init__(self,brand,price,memory,colour,region):
        self.barnd = brand
        self.memory = memory
        self.price = price
        self.colour = colour
        self.region = region
    def run(self):
        return 'Your device is runing'
    

class Laptop(Gadget):
    def __init__(self,memory,brand,price,colour,region):
        self.memory = memory
        super().__init__(brand,price,colour,region,memory)
            
    def conding(self):
        return 'Your code is runing'
    
    def __repr__(self) -> str:
        return f'{self.barnd} is a beautiful its price is {self.price} , its {self.memory} Gb memory , {self.colour} colour and its from {self.region}'
    
    
class Phone(Gadget):
    def __init__(self,dual_sim,brand,price,colour,region):
        self.dual_sim = dual_sim
        super().__init__(brand,price,colour,region)
        
    def phone_call(self,number):
        return f'Your call is going to {number}'
    
class Camera(Gadget):
    def __init__(self,pixel,brand,price,colour,region):
        self.pixel = pixel
        super().__init__(brand,price,colour,region)
        
    def change_lens(self):
        pass
    
hp = Laptop(256,'Hp',126000,'Blue','China')
print(hp)
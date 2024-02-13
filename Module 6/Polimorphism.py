# kono akta function jodi onk jaigai use hoi oittai polimorphism

class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def makes_sound(self):
        print("Makes some sound as usal..")
    
class Cat(Animal):
    def __init__(self, name,nick_name) -> None:
        self.nick_name = nick_name
        super().__init__(name)
        
    def makes_sound(self):
        print("Meow meow ..")
    
class Dog(Animal):
    def __init__(self, name,nick_name) -> None:
        self.nick_name = nick_name
        super().__init__(name)
    def makes_sound(self):
        print("Ghew ghew")
        
Raja = Cat('Catt','Raja Babu')
Raja.makes_sound()

tiger = Dog('DOG mammah ','Tiger khan')
tiger.makes_sound()
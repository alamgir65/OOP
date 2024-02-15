"""
   Aykhane base class and Child class er bitor 'eat' same namer 2ta function create korchi
   amra jokhon access korbo tokhon child class er tai access hobe , its override
"""
class Person:
    def __init__(self,name,age,weight,height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def eat(self):
        print("We eat Burger , Pizza , etc ")
    
    def __repr__(self) -> str:
        print(f"Name : {self.name} , Age : {self.age} Weight : {self.weight} and Height : {self.height}")
        

class Cricketer(Person):
    def __init__(self, name, age, weight, height,team) -> None:
        self.team = team
        super().__init__(name, age, weight, height)
    def eat(self):
        print(self.name , "eat Vegetables")

shakib = Cricketer('Shakib',39,74,5.7,'Rongpur Riders')
muspique = Cricketer('Muspiqur',37,68,5.2,'Fortune Barishal')

shakib.eat()
muspique.eat()
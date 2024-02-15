"""
   shakib and muspique ay 2 ta object er modde kono kichur compare kori tahole error 
   dibe but amra jodi overload functtion use kori tahole r error dibe nah
"""
class Person:
    def __init__(self,name,age,weight,height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    

class Cricketer(Person):
    def __init__(self, name, age, weight, height,team) -> None:
        self.team = team
        super().__init__(name, age, weight, height)
    
    # add indicates '+' operator
    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.height * other.height
    
    def __gt__(self,other):
        return self.age > other.age
    
    def __lt__(self,other):
        return self.age < other.age
    
    

shakib = Cricketer('Shakib',39,74,5.7,'Rongpur Riders')
muspique = Cricketer('Muspiqur',37,68,5.2,'Fortune Barishal')

print(shakib + muspique) 
print(shakib * muspique) 
print(shakib > muspique) 
print(shakib < muspique) 
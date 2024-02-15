class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def eat(self):
        print(self.name, " can eating food")

class Cat(Animal):
    pass
class Dog(Animal):
    pass

c = Cat("Cattu")
c.eat()

d = Dog("Doggu")
d.eat()
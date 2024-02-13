""" amra base class er kono jinish jodi sob class a must be used korte chai tahole abstruct use kori
ata used korle amader must be base class er sob gula function e child class a dite hobe

"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("Love to eating food")
    
    def move(self):
        print("We move in anywhere")
    
class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
        print("hey nana ! I am eating banana")
        
    def eat(self):
        pass
        
michel = Monkey('Meonkey of Michel')
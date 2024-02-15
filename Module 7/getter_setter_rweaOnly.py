# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    @property # use this property convert from methods --> attribute
    def age(self):
        return self._age
    
    @property
    def sallary(self):
        return self.__money
    
    @sallary.setter #kono attributes er value change korte hole attributesname.setter use kora hoi
    def sallary(self,amount):
        if amount < 0:
            return 'Sallary Cannot be negative '
        self.__money += amount
        
me = User('Alamgir',22,400)
print(me.age)

print(me.sallary)

me.sallary = -5000

print(me.sallary)
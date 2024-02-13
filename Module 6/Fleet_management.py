class Company:
    def __init__(self,name,adress,owner):
        self.name = name
        self.adress = adress
        self.owner = owner
        self.drivers = []
        self.passenger = []
        self.manager = []
        self.counter = []
        self.time = []

class Passenger:
    def __init__(self,name,start,destination,time):
        pass

class Drivers:
    def __init__(self,name,license,age,number,expriences):
        self.name = name
        self.license = license
        self.number = number
        self.age = age
        self.expriences = expriences
        print(f'His name is {self.name} , He has a {self.license} and has {self.expriences} , His is {self.age} and his phone number {self.number}')

class Manager:
    def __init__(self,name,adrees,age,number,education):
        pass

kholil = Drivers('Md : Kholil','Valid',43,'34u',2)
print()
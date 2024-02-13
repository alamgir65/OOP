class Family:
    def __init__(self,address,money) -> None:
        self.address = address
        self.money = money
    
    def __repr__(self) -> str:
        return f"This is Family segment --> \n Address: {self.address} and Monthly Cost: {self.money}"

class University:
    def __init__(self,id,course) -> None:
        self.id = id
        self.course = course
    def __repr__(self) -> str:
        return f"This is University segment -->\n id : {self.id} and Course : {self.course}"

class Sports:
    def __init__(self,number,game) -> None:
        self.game = game
        self.number = number
    def __repr__(self) -> str:
        return f"This is Sports Segment --> \n Game : {self.game} Joursey Number : {self.number}"

class Student(Family,University,Sports):
    def __init__(self,name, address, money,course,id,number,game) -> None:
        self.name = name
        # super().__init__(address, money,id,course,number,game)
        Family.__init__(address,money)
        University.__init__(id,course)
        Sports.__init__(number,game)
        
    def __repr__(self) -> str:
        print(f"This is Student Segment -->\n I am {self.name} , Address: {self.address} and Monthly Cost: {self.money}, id : {self.id} and Course : {self.course}, {self.game} Joursey Number : {self.number}")
        return super().__repr__()
        
me = Student('ALamgir','Noakhali',10000,'CSE',131,10,'Cricket')
print(me)
class Company:
    def __init__(self,c_name,location) -> None:
        self.c_name = c_name
        self.location = location
    
    def see_location(self):
        print('Company Name : ', self.c_name, "and Location : ", self.location)
    
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def see_person(self):
        print(f"Name : {self.name} and Age : {self.age}")
        
class Employe(Company,Person):
    def __init__(self,p_name,age,cmp_name,location) -> None:
        Company.__init__(self,cmp_name,location)
        Person.__init__(self,p_name,age)
    
emp = Employe('Alamgir Hossain',22,'Google','USA')

emp.see_location()
emp.see_person()
        
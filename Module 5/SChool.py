class Student:
    def __init__(self,name,c_class,id):
        self.name = name
        self.c_class = c_class
        self.id = id
    def __repr__(self):
        return f'Student name : {self.name}, Class : {self.c_class}, Id : {self.id}'
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f'Teachers name : {self.name} , Subject : {self.subject} , ID : {self.id}'
    
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    
    def enroll(self,name,fee):
        if fee < 6500:
            print('Your money not enough for this course')
        else:
            id = len(self.students)+1
            student = Student(name,'DSA',id)
            self.teachers.append(student)
    
    def __repr__(self):
        print(f'Welcome to our  {self.name} \n')
        print('----Meet OUR Teachers---- \n')
        for x in self.teachers:
            print(x)
        print()
        print('--- Meet OUR STudents ----\n')
        for x in self.students:
            print(x,)
        return 'Well Done'
 
# alamgir = Student('Alamgir Hossain','Hons',131)
# print(alamgir)

# rahat = Teacher('Rahat Khan Pathan','Algorithms',101)
# print(rahat)

phitron = School('CSE Fundamental With Phitron')

phitron.add_teacher('Rahat Khan','DSA')
phitron.add_teacher('Rifat','CP')
phitron.add_teacher('Jhankar Mahbub','OOP and Python')

phitron.enroll('Alamgir ',6500)
phitron.enroll('Tahsin ',10000)
phitron.enroll('Imran',5000)
phitron.enroll('Meem ',10500)

print(phitron)
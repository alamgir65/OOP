def calculate(marks):
        if marks >= 80:
            return 5
        elif marks >= 70:
            return 4
        elif marks >= 60:
            return 3
        elif marks >= 50:
            return 2
        else:
            return 1

class Result:
    def __init__(self):
        self.gpa = 0
        self.min_marks = 40
        self.max_marks = 100
        self.sum = 0
        self.subject = 0
    
    
    
    def add(self,marks):
        if marks < 40:
            print('You fail in your exam')
            self.gpa = 0
        elif marks > 100:
            print('Your marks is insufficient cheak again')
        else:
            x = calculate(marks)
            self.subject += 1
            self.sum += x
            self.gpa = self.sum/(self.subject)
            print(f"Your Gpa is {self.gpa}")
            
alamgir = Result()
alamgir.add(47)
alamgir.add(87)
alamgir.add(57)
alamgir.add(27)
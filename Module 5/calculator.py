class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def subtraction(self,num1,num2):
        return abs(num1-num2)
    def multipication(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        return num1//num2
    
my_calculator = Calculator()
sum = my_calculator.add(2,3)
sub = my_calculator.subtraction(78,3)
mul = my_calculator.multipication(2,3)
div = my_calculator.division(678,3)
print(sum)
print(sub)
print(mul)
print(div)
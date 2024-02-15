class Gradpa:
    def __init__(self) -> None:
        pass
    def grand_property(self):
        print("I have 10 corer Property hahahahah...")

class Father(Gradpa):
    def __init__(self) -> None:
        pass
    def father_property(self):
        print("I have 5 corer property hahaha")
    
    # def grand_property(self):
    #     super().property()
        
class Child(Father):
    def __init__(self) -> None:
        pass
    def my_property(self):
        print("I have 2 corer property haha")
        
me = Child()
me.grand_property()
me.father_property()
me.my_property()
    
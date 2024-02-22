class Book:
    def __init__(self,name,id,quantity) -> None:
        self.name = name
        self.id = id
        self.quantity = quantity

class User:
    def __init__(self,name,id,password) -> None:
        self.name = name
        self.id = id
        self.password = password
        
class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.book_list = []
        self.user_list = []

    
    def add_book(self,name,id,quantity):
        book = Book(name,id,quantity)
        flag = False
        for x in self.book_list:
            if x.id == id:
                x.quantity += quantity
                flag = True
                
        if flag == False:
            self.user_list.append(book)
        print("Your book successfully added")
        
    def add_user(self,name,id,password):
        flag = False
        for x in self.user_list:
            if x.id == id:
                flag=True
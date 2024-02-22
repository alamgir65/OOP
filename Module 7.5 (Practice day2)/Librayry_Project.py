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
        self.borrowedBook = []
        self.returnedBook = []
    
class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.books = []
        self.users = []
    
    def addBook(self,name,id,quantity):
        book = Book(name,id,quantity)
        self.books.append(book)
        print(f"{name} this book added successfull")
        
    def addUser(self,name,id,password):
        user = User(name,id,password)
        self.users.append(user)
        print(f"{name} this user added successfull")
        
    def BorrowBook(self,user,Id):
        for book in self.books:
            if book.id == Id:
                if book in user.borrowedBook:
                    print("This book already exists in your borrowed list")
                    return
                elif book.quantity == 0:
                    print("This book is not available now")
                    return
                else:
                    user.borrowedBook.append(book)
                    book.quantity -= 1
                    print(f"{book.name} This book added borrowed list")
                    return
        print(f"This is not Available now !")
    
    def returnBook(self,user,Id):
        for book in self.books:
            if book in user.borrowedBook:
                if book.id == Id:
                    print("This book is return successfully")
                    user.borrowedBook.remove(book)
                    user.returnedBook.append(book)
                    book.quantity += 1
                    return
                else:
                    print(f"{book.name} This book is not yet you read")
                    return
        print(f"This is not Available now !")

bks = Library("Bishaw Shahitto kendro")

physics = bks.addBook('Physics',1001,100)
chemistry = bks.addBook('Chemistry',1002,50)
algorithm = bks.addBook('Algorithms',1003,10)

admin = bks.addUser('admin',111,'admin')
alamgir = bks.addUser('alamgir',222,'alamgir')

currentuser = alamgir

while True:
    if currentuser == None:
        print("No login user \n")
        op = input("Enter Option L/R : ")
        
        if op == 'L':
            id = int(input("enter Your id : "))
            password = (input("enter Your password : "))
            match = False
            for user in bks.users:
                if id == user.id and password == user.password:
                    currentuser = user
                    break
            if match == False:
                print("Incorrect Your id or Password")
            else:
                print("Your Login Successfull")
                
        elif op == 'R':
            name = input("Enter Your name : ")
            id = int(input("enter Your id : "))
            password = (input("enter Your password : "))
            match = False
            for i in bks.users:
                if id == user.id:
                    match = True
            
            if match == True:
                print("This Id is already exists")
            else:
                user = bks.addUser(name,id,password)
                currentuser = user
                
    else:
        print(f"Thanks! {currentuser.name} for Successfully Login")
        
        if currentuser.name == 'admin':
            print("Option 1: Add book")
            print("Option 2: Add User")
            print("Option 3: Show all Books")
            print("Option 4: Log out")
            
            option = int(input("Enter Option : "))
            if option == 1:
                name = input("Enter book name : ")
                id = int(input("Enter book id : "))
                quantity = int(input("Enter quantity : "))
                bks.addBook(name,id,quantity)
                
            elif option == 2:
                name = input("Enter Your name : ")
                id = int(input("enter Yor id : "))
                password = (input("enter Yor id : "))
                bks.addUser(name,id,password)
                
            elif option == 3:
                for book in bks.books:
                    print(f"{book.name}, id -> {book.id} , quantity -> {book.quantity}")
                print('\n')
            else:
                currentuser = None
        
        else:
            print("Option 1: Borrow Book")
            print("Option 2: Returned Book")
            print("Option 3: Show all Borrowed Books")
            print("Option 4: Show all Returned Books")
            print("Option 5: Log out")
            
            op = int(input("Enter your option : "))
            
            if op == 1:
                id = int(input("Enter Book id : "))
                bks.BorrowBook(currentuser,id)
            elif op == 2:
                id = int(input("Enter Book id : "))
                bks.returnBook(currentuser,id)
            elif op == 3:
                for book in currentuser.borrowedBook:
                    print(f"{book.name}, id -> {book.id} , quantity -> {book.quantity}")
                print('\n')
            elif op == 4:
                for book in currentuser.returnedBook:
                    print(f"{book.name}, id -> {book.id} , quantity -> {book.quantity}")
                print('\n')
            else:
                currentuser = None
                
            
            
    
    
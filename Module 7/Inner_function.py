# Amra chaile akta function er bitor arekta function declare korte pari such that -->

def outer_fun():
    print("Hey Dounble Diccker ")
    def inner_func():
        print("Hey inner unction kiya hal he apka ?? ")
        return 'Iya mera inner ka return hain '
    return inner_func

print(outer_fun()())


# Amra chaile akta function er bitor arekta function parameter hishabe dite pari such that -->

def fun(work):
    print("Before Working ")
    
    work()
    
    print("After Working")
    
def hello():
    print("I am relaxing for sometime ")

fun(hello)
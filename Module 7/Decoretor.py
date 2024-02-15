import math
import time
def timer(func):
    start = time.time()
    def inner(*args,**kwargs):
        print("Time Started ->")
        func(*args,**kwargs)
        print("Time Ended")
    end = time.time()
    print(f"Time taken : {end-start}")
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is : {result}")

get_factorial(n=1200)
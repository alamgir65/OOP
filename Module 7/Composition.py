class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        print("Start your Engine")
        
class Driver:
    def __init__(self) -> None:
        pass
    def run(self):
        print("Car can not run without driver")

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
    
    def start(self):
        self.engine.start()
    
car = Car()
car.start()
car.driver.run()
"""onek gula choto class aksathe hoye je boro akta class create kore tare composition bole"""


class Cpu:
    def __init__(self,cores) -> None:
        self.cores = cores
    
class Ram:
    def __init__(self,size) -> None:
        self.size = size

class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
    
class Computer:
    def __init__(self,corer,sizE,capacitY) -> None:
        self.cpu = Cpu(corer)
        self.ram = Ram(sizE)
        self.hdrive = HardDrive(capacitY)

mac = Computer(8,16,512)
print(mac.cpu , mac.hdrive , mac.ram)
    
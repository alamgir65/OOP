class Shopping:
    def __init__(self,name,location):
        self.name = name
        self.location =location
    
    @staticmethod
    def cheak_static(item):
        print('Hudai print korlam r ki',item)
    
    @classmethod
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f"After buying your balan is" , remaining)
    
# Shopping.purchase('self','lungi',800,1500) #before using @classmethods
Shopping.purchase('lungi',800,1500) #before using @classmethods

Shopping.cheak_static('Hey mammah') #statice attribute use korai self lage nai
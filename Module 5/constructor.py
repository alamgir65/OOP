class Phone:
    manufactured = 'China'
    # Constructor
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    def send_sms(self,phone,sms):
        text = f'who send me this message from {phone} this phone , and send {sms} this sms'
        print(text)
        
my_phone = Phone('Alamgir','Vivo',12500)
shamim_phone = Phone('Shamim ','Oppo',11000)
dad_phone = Phone('Baba','Nokia',1200)
print(my_phone.name, my_phone.brand,my_phone.price,sep=' --> ')
print(shamim_phone.name , shamim_phone.brand ,shamim_phone.price, sep=' --> ')
print(dad_phone.name , dad_phone.brand ,dad_phone.price, sep=' --> ')
def call():
    print('Call him !!')
    return 'Call Done!'

class Phone:
    name = 'Vivo'
    price = 12500
    colour = 'Bule'
    features = ['Camera','Speaker','High volum']
    # class er bitor amra kono function ba methods ke kono parameter na dile ata call hobe nah
    # such as -->
    # def call():
    #     print("Calling one person")
    
    #aykarone amra self akta parameter pass kori
    def call(self):
        print("Calling one person")
    
    #function a always 1st parameter ta ke self hisabe niye nei, ay jonno amra always extra parameter pass kori
    def send_msg(self,phone,sms):
        text = f'send this message -> {sms} in this number -> {phone}'
        print(text)
my_phone = Phone()
print(my_phone.name)
# print(my_phone.call())
my_phone.call()
rechieve = call()

my_phone.send_msg('01868194925','Hey janu')
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
   

    def sayName(self):
        print("меня зовут ", self.first_name)

    def saySurname(self):
        print("моя фамилия ", self.last_name)

    def sayFullname(self):
         print(f'моё полное имя: {self.first_name} {self.last_name}')
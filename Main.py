import random
class Person:
    def __init__(self, name, surname, age, balance, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.balance = balance
        self.id = id
        self.password = password
        if self.age >= 65:
            self.balance = self.balance + 2000
            print("К балансу добавлено 2000 доп. бонусов")
    def password_verification(self):
        password = int(input("Введите парооль для входа: "))
        if password == self.password:
            print("Вы успешно выполнили вход!")
        else:
            print("Неверный пароль")
    def indification(self):
        name = input("Введите ваше имя для проверки: ")
        surname = input("Введите вашу фамилию для проверки: ")
        if name == self.name and surname == self.surname:
            print("Вы ввели правильные данные")
        else:
            print("Неправильные данные")
            return 0
    def transaction(self):
        print(self.balance)
        sum = float(input("Введите сумму перевода: "))
        reciever = input("Введите получателя: ")
        reciever2 = input("Введите пользователя для проверки:")
        if reciever2 == reciever:
            print("Пользователь подтвержден")
        if sum > self.balance:
            return 0
        elif sum > 10000:
            com = sum / 10
            print(f"Комиссия составила: {com}")
            if sum + com > self.balance:
                return 0
            self.balance = self.balance - (sum + com)
            if len(reciever) > 10:
                sum = sum + 250
                print("К сумме перевода начислены подарочные 250 бонусов")
            print(f"Вы уcпешно перевели сумму в размере: {sum + com}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
        elif sum <= 0:
            return 0
        else:
            self.balance = self.balance - sum
            if len(reciever) > 10:
                sum = sum + 250
                print("К сумме перевода начислены подарочные 250 бонусов")
            print(f"Вы уcпешно перевели сумму в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
    def check_id(self):
        print(f"Ваш id: {self.id}")



name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
wallet = random.randint(1, 300001)
id = random.randint(1, 10000)
password = int(input("Введите пароль: "))
a = Person(name, surname, age, wallet, id)
a.password_verification()
a.indification()
a.transaction()
a.check_id()

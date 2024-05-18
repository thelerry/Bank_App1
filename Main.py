import random
class Person:
    def __init__(self, name, surname, age, balance, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.balance = balance
        self.id = id
        if self.age >= 65:
            self.balance = self.balance + 2000
            print("К балансу добавлено 2000 доп. бонусов")

    def transaction(self):
        sum = float(input("Введите сумму перевода: "))
        reciever = input("Введите получателя: ")
        print(self.balance)
        if sum > self.balance:
            return 0
        elif sum > 300000:
            com = sum / 10
            print(com)
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
a = Person(name, surname, age, wallet, id)
a.transaction()
a.check_id()
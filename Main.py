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
        password = int(input("Введите пароль для входа: "))
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
            exit(1)
    def transaction(self):
        file = open("transactions.txt","w+")
        Sponsors = ["Sberbank", "Magnit", "Letual", "Golden Apple", "Gazprom", "Aeroflot", "Metro", "Ashan", "Leroumerlen", "Pyaterochka", "Ikea", "Fix-price", ]
        i = 0
        print(f"Ваш текущий баланс: {self.balance}")
        pincode = random.randint(1, 99999)
        print(f"Ваш пинкод: {pincode}")
        sum = float(input("Введите сумму перевода: "))
        reciever = input("Введите получателя: ")
        reciever2 = input("Введите получателя для проверки: ")
        if reciever == Sonsors[i]:
            self.balance = self.balance + 1000
            print(f"Ваш новый баланс с учетом бонусов от спонсоров составил: {self.balance}")
            if reciever2 == reciever:
                print("Получатель подтвержден")
                pincode2 = int(input("Введите пинкод: "))
                if pincode == pincode2:
                    print("Верный пинкод")
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
                        file.write(f"Сумма в размере: {sum + com}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                    elif sum <= 0:
                        return 0
                    else:
                        self.balance = self.balance - sum
                        if len(reciever) > 10:
                            sum = sum + 250
                            print("К сумме перевода начислены подарочные 250 бонусов")
                        print(f"Вы уcпешно перевели сумму в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                        file.write(f"Сумма в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                else:
                    print("Неверный пинкод")
                    exit(1)
            else:
                print("Неверный получатель")
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
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
            print("К балансу добавлено 2000 доп. пенсионных бонусов")
        self.password = password
    def password_verification(self):
        password = input("Введите пароль для входа: ")
        f = ""
        t = False
        d = ["#", "%", "?", "@", "/"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        flag = False
        y = input("Введите пароль заново: ")
        while True:
            if len(y) < 8:
                print("Слишком короткий пароль")
                y = input("Введите пароль заново: ")
            else:
                for i in d:
                    if i in y:
                        t = True
                        f = str(i)
                if t == True:
                    print(f"Найден запрещенный символ - {f}")
                    y = input("Введите пароль заново: ")
                    t = False
                for i in numbers:
                    if i in y:
                        flag = True
                if flag == False:
                    print("Ненадежный пароль")
                    y = input("Введите пароль заново: ")
                    flag = False
                else:
                    break
        if password == y:
            print("Вы успешно выполнили вход!")
        else:
            print("Неверный пароль")
            exit(1)
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
        Sponsors = ["Sberbank", "Magnit", "Golden Apple", "Gazprom", "Aeroflot", "Metro", "Ashan", "Pyaterochka", "Ikea", "Fix-price", ]
        i = 0
        print(f"Ваш текущий баланс: {self.balance}")
        pincode = random.randint(1, 99999)
        print(f"Ваш пинкод: {pincode}")
        pincode2 = int(input("Введите пинкод: "))
        if pincode2 == pincode:
            print("Верный пинкод")
            sum = float(input("Введите сумму перевода: "))
            reciever = input("Введите получателя: ")
            reciever2 = input("Введите получателя для проверки: ")
            if reciever2 == reciever:
                print("Получатель подтвержден")
                if len(reciever) > 10:
                    sum = sum + 250
                    print("К сумме перевода начислены 250 доп. единиц")
                if reciever == Sponsors[i]:
                    self.balance = self.balance + 1000
                    print(f"Ваш новый баланс с учетом бонусов от спонсоров составил: {self.balance}")
                if sum > self.balance:
                    return 0
                elif sum > 10000:
                    com = sum / 10
                    print(f"Комиссия составила: {com}")
                    if sum + com > self.balance:
                        return 0
                    self.balance = self.balance - (sum + com)
                    confirm = input("Вы подтверждаете перевод средств?\n")
                    if confirm == "Да":
                        print(
                            f"Вы уcпешно перевели сумму в размере: {sum + com}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                        file.write(
                            f"Сумма в размере: {sum + com}\nПользователь: {reciever}\nВаш баланс: {self.balance}\n")
                elif sum <= 0:
                    return 0
                else:
                    self.balance = self.balance - sum
                    confirm = input("Вы подтверждаете перевод средств?\n")
                    if confirm == "Да" or "Yes":
                        print(
                            f"Вы уcпешно перевели сумму в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                        file.write(f"Сумма в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}\n")
            else:
                print("Неверный получатель")
        else:
            print("Неверный пинкод")
    def check_id(self):
        print(f"Ваш id: {self.id}")

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
wallet = random.randint(1, 300001)
id = random.randint(1, 10000)
password =()
a = Person(name, surname, age, wallet, id)
a.password_verification()
a.indification()
a.transaction()
a.check_id()
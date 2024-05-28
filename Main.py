import random
class Person:
    def __init__(self, name, surname, age, balance, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.balance = balance
        self.id = id
        self.password = password
        if self.age >= 65 and self.age <=70:
            self.balance = self.balance + 2000
            print("К балансу добавлено 2000 доп.пенсионных бонусов")
        if self.age > 70:
            print("Вы не можете быть пользователем нашего банка")
            exit(1)

    def password_verification(self):
        d = ["$", "*", "№", "#", "%", "?", "\", /"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        password = input("Введите пароль: ")
        if len(password) < 8:
            print("Слишком короткий пароль")
        password = input("Введите пароль заново: ")
        for i in d:
            if i in password:
                print(f"Найден запрещенный символ:{i}\nВы использовали максимальное число попыток\nПопробуйте повторить позже")
                exit(1)
        else:
            print("Надежный пароль")

    def password_checking(self):
        password_01 = input("Повторно введите ваш пароль: ")
        password_2 = input("Введите пароль для входа: ")
        if password_2 == password_01:
            print("Верный пароль!")
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
password = ()
a = Person(name, surname, age, wallet, id)
a.password_verification()
a.password_checking()
a.indification()
a.transaction()
a.check_id()
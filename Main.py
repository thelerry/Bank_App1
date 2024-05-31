import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bank App")
window.geometry('400x300')
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
            frame = Frame(window,padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="К балансу добавлено 2000 доп.пенсионных бонусов")
            test_lb.grid(row=5, column=1)

        if self.age > 70:
            frame = Frame(window, padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Вы не можете быть пользователем нашего банка")
            test_lb.grid(row=5, column=1)
            exit(1)



    def password_verification(self):
        d = ["$", "*", "№", "#", "%", "?", "/"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        password = input("Введите пароль: ")
        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)
        test_lb = Label(frame, text=password)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)
        if len(password) < 8:
            frame = Frame(window, padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Слишком короткий пароль")
            test_lb.grid(row=5, column=1)
        password = input("Введите пароль заново: ")
        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)
        test_lb = Label(frame, text=password)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)
        for i in d:
            if i in password:
                frame = Frame(window, padx=10, pady=10)
                frame.pack(expand=True)
                test_lb = Label(frame, text=f"Найден запрещенный символ:{i}\nВы использовали максимальное число попыток\nПопробуйте повторить позже")
                exit(1)
        else:
            frame = Frame(window, padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Надежный пароль")

    def password_checking(self):
        password_01 = input("Повторно введите ваш пароль: ")
        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)
        test_lb = Label(frame, text=password_01)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)

        password_2 = input("Введите пароль для входа: ")
        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)
        test_lb = Label(frame, text=password_2)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)

        if password_2 == password_01:
            frame = Frame(window, padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Верный пароль!")
            test_lb.grid(row=5, column=1)
        else:
            frame = Frame(window, padx=10, pady=10)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Неверный пароль!")
            test_lb.grid(row=5, column=1)
            exit(1)
    def indification(self):
        name = input("Введите ваше имя для проверки: ")
        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=name)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)

        surname = input("Введите вашу фамилию для проверки: ")
        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=surname)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)

        if name == self.name and surname == self.surname:
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Вы ввели правильные данные")

        else:
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Неправильные данные")
            exit(1)
    def transaction(self):
        file = open("transactions.txt","w+")
        print(f"Ваш текущий баланс: {self.balance}")
        Sponsors = ["Sberbank", "Magnit", "Golden Apple", "Gazprom", "Aeroflot", "Metro", "Ashan", "Pyaterochka", "Ikea", "Fix-price", ]
        i = 0
        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=f"Ваш текущий баланс: {self.balance}")
        test_lb.grid(row=5, column=1)

        pincode = random.randint(1, 99999)
        print(f"Ваш пинкод: {pincode}")
        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=f"Ваш пинкод: {pincode}")
        test_lb.grid(row=5, column=1)

        pincode2 = int(input("Введите пинкод: "))
        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=pincode2)
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)

        if pincode2 == pincode:
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Верный пинкод")

            sum = float(input("Введите сумму перевода: "))
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text=sum)
            test_lb.grid(row=5, column=1)
            test_ent = Entry(frame)
            test_ent.grid(row=3, column=2)

            reciever = input("Введите получателя: ")
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text=reciever)
            test_lb.grid(row=5, column=1)
            test_ent = Entry(frame)
            test_ent.grid(row=3, column=2)

            reciever2 = input("Введите получателя для проверки: ")
            frame = Frame(window, padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text=reciever2)
            test_lb.grid(row=5, column=1)
            test_ent = Entry(frame)
            test_ent.grid(row=3, column=2)

            if reciever2 == reciever:
                frame = Frame(window, padx=10, pady=12)
                frame.pack(expand=True)
                test_lb = Label(frame, text="Получатель подтвержден")
                test_lb.grid(row=5, column=1)

                if len(reciever) > 10:
                    sum = sum + 250
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text="К сумме перевода начислены 250 доп. единиц")
                    test_lb.grid(row=5, column=1)

                if reciever == Sponsors[i]:
                    self.balance = self.balance + 1000
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=f"Ваш новый баланс с учетом бонусов от спонсоров составил: {self.balance}")
                    test_lb.grid(row=5, column=1)

                if sum > self.balance:
                    return 0
                elif sum > 10000:
                    com = sum / 10
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=f"Комиссия составила: {com}")
                    test_lb.grid(row=5, column=1)
                    if sum + com > self.balance:
                        return 0
                    self.balance = self.balance - (sum + com)
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=self.balance)
                    test_lb.grid(row=5, column=1)

                    confirm = input("Вы подтверждаете перевод средств?\n")
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=confirm)
                    test_lb.grid(row=5, column=1)
                    test_ent = Entry(frame)
                    test_ent.grid(row=3, column=2)

                    if confirm == "Да" or 'Yes':
                        frame = Frame(window, padx=10, pady=12)
                        frame.pack(expand=True)
                        test_lb = Label(frame, text=f"Вы уcпешно перевели сумму в размере: {sum + com}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                        test_lb.grid(row=5, column=1)

                elif sum <= 0:
                    return 0
                else:
                    self.balance = self.balance - sum
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=self.balance)
                    test_lb.grid(row=5, column=1)

                    confirm = input("Вы подтверждаете перевод средств?\n")
                    frame = Frame(window, padx=10, pady=12)
                    frame.pack(expand=True)
                    test_lb = Label(frame, text=confirm)
                    test_lb.grid(row=5, column=1)
                    test_ent = Entry(frame)
                    test_ent.grid(row=3, column=2)

                    if confirm == "Да" or "Yes":
                        frame = Frame(window, padx=10, pady=12)
                        frame.pack(expand=True)
                        test_lb = Label(frame, text=f"Вы уcпешно перевели сумму в размере: {sum}\nПользователь: {reciever}\nВаш баланс: {self.balance}")
                        test_lb.grid(row=5, column=1)

            else:
                frame = Frame(window, padx=10, pady=12)
                frame.pack(expand=True)
                test_lb = Label(frame,text="Неверный получатель")
                test_lb.grid(row=5, column=1)
        else:
            frame = Frame(window,padx=10, pady=12)
            frame.pack(expand=True)
            test_lb = Label(frame, text="Неверный пинкод")
            test_lb.grid(row=5, column=1)
    def check_id(self):

        frame = Frame(window, padx=10, pady=12)
        frame.pack(expand=True)
        test_lb = Label(frame, text=f"Ваш id: {self.id}")
        test_lb.grid(row=5, column=1)
        test_ent = Entry(frame)
        test_ent.grid(row=3, column=2)


name = input("Введите имя: ")
frame = Frame(window, padx=10, pady=12)
frame.pack(expand=True)
test_lb = Label(frame, text = name)
test_lb.grid(row=5, column=1)
test_ent = Entry(frame)
test_ent.grid(row = 3, column = 2)

surname = input("Введите фамилию: ")
frame = Frame(window, padx=10, pady=12)
frame.pack(expand=True)
test_lb = Label(frame, text=surname)
test_lb.grid(row=5, column=1)
test_ent = Entry(frame)
test_ent.grid(row=3, column=2)

age = int(input("Введите возраст: "))
frame = Frame(window, padx=10, pady=12)
frame.pack(expand=True)
test_lb = Label(frame, text=age)
test_lb.grid(row=5, column=1)
test_ent = Entry(frame)
test_ent.grid(row=3, column=2)

wallet = random.randint(1, 300001)
id = random.randint(1, 10000)
password = ()
a = Person(name, surname, age, wallet, id)
a.password_verification()
a.password_checking()
a.indification()
a.transaction()
a.check_id()
window.mainloop()
# result = 0

# while True:
#     number = int(input('Enter number or Enter -1 to exit: '))

#     if number == -1:
#         break
#     result = result + number
#     print(f"Result: {result}")

# while True:
#     number = int(input("Enter number (or -1 to exit): "))

#     if number == -1:
#         print("Programm los.")
#         break

#     if number % 2 == 0:
#         print(f"Number {number} - /2 ")
#     else:
#         print(f"Number {number} - ne /2")

# ochen = 0
# one = 0

# while True:
#     Inp = input("Enter number: ")
#     if Inp == "0":
#         if one > 0:
#             print("res: " + str(ochen // one))
#         else:
#             print("No numbers entered")
#         break
#     one += 1
#     ochen += int(Inp)

# correct_password = "secret123"

# while True:
#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Welcome!")
#         break
#     else:
#         print("No No No No go na h...")

# n = int(input('Enter number: '))

# print(f"Тамблица умножения на {n}")
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# n = int(input('Enter size n: '))
# a = int(input('Enter size a: '))

# for i in range(n):
#     print('*' * a)

# n = str(input('Enter: '))

# for i in n:
#     print(i)

# symvol = input('Enter simvol: ')
# text = input('Enter stroka: ')

# count = 0

# for char in text:
#     if char == symvol:
#         count += 1

# print(f"Символ {symvol} встречается {count} раз(а)")

# mass = ['Apple', 'Grusha', 'Markva', 'Kipusta', 'Yagoda brat vkusnaya beri']

# mass.append('Beralus')
# mass.append('Net')
# mass.pop(2)

# print(mass)

# n = int(input('Enter number n: '))

# numbers = list(range(1, n + 1))

# print(numbers)

# n = int(input('Enter numbers n: '))
# numbers = [i for i in range(2, n + 1, 2)]
# print(numbers)

# def HelloWorld(command):
#     if command == 'print':
#         exec('print("HelloWorld")')
# HelloWorld('print')

# home
# patname = str(input('Enter youre pet name: '))
# patage = int(input('Enter pet age: '))

# print(f'Имя питомца: {patname}')
# # print(f'Возраст питомца: {patage}')

# if patage == 1:
#     print('Возраст питомца: 1 год')
# elif patage >= 2 and patage < 5:
#     print(f'Возраст питомца: {patage} года')
# elif patage >= 5:
#     print(f'Возраст питомца: {patage} лет')
# else:
#     print('Error code')


# t = input('Enter text: ')

# print((t + '\n') * 100)


# import random

# coin = ["Орёл - нужно переименовать горку", "Решка - нужно демонтировать горку"]

# result = random.choice(coin)
# print(f"Итог: {result}")


# clas = ["Алгебра", "Геометрия", "Русский"]

# while True:
#     print("")
#     print('Выберите действие: 1 - Посмотреть уроки 2 - Внести урок 3 - Удалить урок 4 - выход из программы')
#     n = int(input(": "))

#     if n == 1:
#         print("")
#         print(clas)
#         print("")
#     elif n == 2:
#         print("")
#         a = input("Какой урок внести? ")
#         clas.append(a)
#         print("")
#         print("Сделано!")
#         print("")
#         print(clas)
#     elif n == 3:
#         print("")
#         d = input("Какой урок удалить? ")
#         clas.remove(d)
#         print("")
#         print("Сделано!")
#         print("")
#         print(clas)
#     elif n == 4:
#         print("")
#         print("Выход из программы")
#         print("")
#         break
#     else:
#         print("Error")


# slide1 = {'name': "Kantemir", 'lenght': 300}
# slide2 = {'name': "Kantir", 'lenght': 501}
# slide3 = {'name': "Kantr", 'lenght': 5}
# slide4 = {'name': "Kantem", 'lenght': 100}

# slides = [slide1, slide2, slide3, slide4]
# lens = len(slides)
# asw = int(input("Enter number: "))
# print(slides[asw - 1])


# slide = slides[0]['lenght']
# print(slide)


# film = {
#     "Комедия": ["Один дома", "Сваты"],
#     "Драма": ["Форрест Гамп", "Король говорит"],
#     "Фантастика": ["Интерстеллар", "Матрица", "Грань будущего", "Начало"],
#     "Боевик": ["Крепкий орешек", "Терминатор"]
# }

# print(film["Фантастика"][-1])


# slides = [
#     {
#         "название": "Детская",
#         "высота": 8,
#         "скорость": 25,
#         "длина": 150,
#     },
#     {
#         "название": "Средняя",
#         "высота": 22,
#         "скорость": 60,
#         "длина": 480,
#     },
#     {
#         "название": "Взрослая",
#         "высота": 45,
#         "скорость": 95,
#         "длина": 920,
#     },
#     {
#         "название": "Аквамарин",
#         "высота": 18,
#         "скорость": 40,
#         "длина": 320,
#     },
#     {
#         "название": "Посейдон",
#         "высота": 35,
#         "скорость": 75,
#         "длина": 680,
#     },
# ]


# print("🎢 ИНФОРМАЦИЯ О ГОРКАХ")
# print("=" * 40)

# for slide in slides:
#     print(f"\n🏗️  {slide['название']}")
#     print(f"   📏 Высота: {slide['высота']} м")
#     print(f"   🚀 Скорость: {slide['скорость']} км/ч")
#     print(f"   📐 Длина: {slide['длина']} м")
#     print("-" * 30)



# from random import randint

# def card_num():
#     number = randint(1000000000000000, 9999999999999999)
#     return number

# def card_ye(month, year):

#     ex_year = year + 4
    
#     ex_month = month
    
#     print(f"Срок действия карты: 31/{ex_month:02d}/{ex_year}")

# print(f"Номер вашей карты: {card_num()}")

# month = 10
# year = 2025

# card_ye(month, year)



# from random import randint

# def get_number():
#     number = randint(1000000000000000, 9999999999999999)
#     while number in numbers:
#         number = randint(1000000000000000, 9999999999999999)
#     numbers.append(number)
#     print(f"Текущий номер карты: {number}")
#     return number

# numbers = []
# print(f"Номер вашей карты: {get_number()}")



# def calc_perimeter(width, height):
#     perimeter = 2 * (width + height)
#     return perimeter

# def calc_area(width, height):
#     area = width * height
#     return area

# if __name__ == "__main__":
#     width = 5
#     height = 3
    
#     perimeter = calc_perimeter(width, height)
#     area = calc_area(width, height)
    
#     print(f"Прямоугольник: ширина = {width}, высота = {height}")
#     print(f"Периметр: {perimeter}")
#     print(f"Площадь: {area}")

print("Продам гараж")


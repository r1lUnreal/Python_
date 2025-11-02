number = input("Введите число: ")
sum_senior = 0

for digit in number:
    sum_senior += int(digit)

print(f"Сумма цифр числа = {sum_senior}")

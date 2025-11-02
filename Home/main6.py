n = int(input("Введите число n: "))
sum_junior = 0

for i in range(1, n + 1):
    sum_junior += i

print(f"Сумма чисел от 1 до {n} = {sum_junior}")

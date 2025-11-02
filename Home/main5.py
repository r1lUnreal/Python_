num = int(input('Enter number: '))

if num < 2:
    print(f"{num} - composite number")
else:
    tr = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tr = False
            break

    if tr:
        print(f"{num} - a prime number")
    else:
        print(f"{num} - composite number")

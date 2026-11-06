limit = int(input("Введите число N: "))
if limit <= 0:
    print("Нужно положительное целое число")
else:
    current = 1
    while current <= limit:
        print(current)
        current += 1

contributions = []

while True:
    amount = int(input("Введите сумму (0 — закончить): "))
    if amount == 0:
        break
    if amount < 0:
        continue
    contributions.append(amount)

if contributions:
    print("Суммы в копилке:", *contributions)
else:
    print("Копилка пуста, вы не положили ни рубля")

print("Количество взносов:", len(contributions))
print("Общая сумма:", sum(contributions))

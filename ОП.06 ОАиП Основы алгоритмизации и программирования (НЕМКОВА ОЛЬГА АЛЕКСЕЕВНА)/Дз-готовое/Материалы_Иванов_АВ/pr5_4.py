seconds = int(input("Количество секунд: "))
hours = int(seconds / 3600)
remainder = seconds % 3600
minutes = int(remainder / 60)
last_seconds = remainder % 60
print("Часов:", hours)
print("Минут:", minutes)
print("Секунд:", last_seconds)
print("Дробное число часов:", seconds / 3600)

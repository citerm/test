homework_done = input("Уроки сделаны? (да/нет): ").strip().lower() == "да"
snowing = input("Идёт снег? (да/нет): ").strip().lower() == "да"
if homework_done and not snowing:
    print("Можно гулять")
else:
    print("Прогулку отложим")

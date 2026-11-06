import random
secret = random.randint(1, 100)
attempts = 0
print("Загадано число от 1 до 100")
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess == secret:
        print("Поздравляю! Вы угадали!")
        print("Количество попыток:", attempts)
        break
    elif guess < secret:
        print("Слишком мало!")
    else:
        print("Слишком много!")

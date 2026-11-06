phrase = input("Введите строку: ")
vowel_count = 0
for letter in phrase:
    if letter.lower() in "аеёиоуыэюяaeiouy":
        vowel_count += 1
print("Гласных:", vowel_count)
print("Каждый третий символ:")
for position, letter in enumerate(phrase):
    if position % 3 == 2:
        print(f"Индекс {position}: {letter!r}")
print("Символов всего:", len(phrase))

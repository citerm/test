from pathlib import Path
import io,contextlib,json,builtins,random
from unittest.mock import patch
ROOT=Path(__file__).resolve().parent
codes={
'pr4':'''name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
message = "Меня зовут " + name + ", мне " + age + " лет"
print(message)
''',
'pr5_1':'''length = float(input("Длина, см: "))
width = float(input("Ширина, см: "))
perimeter = 2 * (length + width)
area = length * width
print("Периметр:", perimeter, "см")
print("Площадь:", area, "кв. см")
''',
'pr5_2':'''first = float(input("Первое число: "))
second = float(input("Второе число: "))
third = float(input("Третье число: "))
mean = (first + second + third) / 3
print("Среднее:", mean)
''',
'pr5_3':'''pens = int(input("Сколько ручек? "))
pencils = int(input("Сколько карандашей? "))
total = 9.5 * pens + 7 * pencils
print("К оплате:", total, "руб.")
''',
'pr5_4':'''seconds = int(input("Количество секунд: "))
hours = int(seconds / 3600)
remainder = seconds % 3600
minutes = int(remainder / 60)
last_seconds = remainder % 60
print("Часов:", hours)
print("Минут:", minutes)
print("Секунд:", last_seconds)
print("Дробное число часов:", seconds / 3600)
''',
'pr7_walk':'''homework_done = input("Уроки сделаны? (да/нет): ").strip().lower() == "да"
snowing = input("Идёт снег? (да/нет): ").strip().lower() == "да"
if homework_done and not snowing:
    print("Можно гулять")
else:
    print("Прогулку отложим")
''',
'pr8_1':'''limit = int(input("Введите число N: "))
if limit <= 0:
    print("Нужно положительное целое число")
else:
    current = 1
    while current <= limit:
        print(current)
        current += 1
''',
'pr8_2':'''import random
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
''',
'pr9_1':'''for left in range(5, 0, -1):
    row = ""
    for right in range(5, 0, -1):
        row += f"{left} * {right} = {left * right:2d}   "
    print(row.rstrip())
''',
'pr9_2':'''phrase = input("Введите строку: ")
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
'''}

def run(code,inputs=(),secret=None):
    it=iter(map(str,inputs));out=io.StringIO()
    def answer(prompt=''):
        x=next(it);print(prompt+x);return x
    with contextlib.redirect_stdout(out),patch('builtins.input',answer):
        if secret is None:exec(compile(code,'<student program>','exec'),{})
        else:
            with patch('random.randint',return_value=secret):exec(code,{})
    return out.getvalue().rstrip()

tests={
'pr4':[['Антон',22],['Олег',19]],
'pr5_1':[[7.5,4],[1,1]],'pr5_2':[[-6,3,12],[0,0,0]],
'pr5_3':[[4,3],[0,2]],'pr5_4':[[7328],[3665],[59],[3600],[0]],
'pr7_walk':[['да','нет'],['да','да'],['нет','нет']],
'pr8_1':[[6],[1],[0]],'pr8_2':[[40,80,64],[64]],
'pr9_1':[[]], 'pr9_2':[['Учусь в МТУСИ!'],['AEy Ёж'],[''],['абвгдеёжз']]}
results={}
for name,code in codes.items():
    (ROOT/(name+'.py')).write_text(code,encoding='utf-8')
    results[name]=[{'input':inp,'output':run(code,inp,64 if name=='pr8_2' else None)} for inp in tests[name]]
assert 'Индекс 2' in results['pr9_2'][0]['output']
assert 'Секунд: 5' in results['pr5_4'][1]['output'] and 'Минут: 1' in results['pr5_4'][1]['output']
assert results['pr9_2'][2]['output'].endswith('Символов всего: 0')
assert 'Количество попыток: 3' in results['pr8_2'][0]['output']
(ROOT/'program_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
cells=[]
for key in ['pr5_1','pr5_2','pr5_3','pr5_4']:
    cells.append({'cell_type':'code','metadata':{},'source':codes[key].splitlines(True),'execution_count':None,'outputs':[]})
(ROOT/'Практическая_5_Иванов_АВ.ipynb').write_text(json.dumps({'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},'nbformat':4,'nbformat_minor':5},ensure_ascii=False,indent=2),encoding='utf-8')
print('Проверено запусков:',sum(map(len,results.values())))
print(results['pr9_2'][0]['output'])

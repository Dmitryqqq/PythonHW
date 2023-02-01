# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint

x = randint(0,1000)
y = randint(0,1000)
print(f"Загаданные числа это {x} и {y}")
s = x + y
p = x * y
print("Сумма  ",s)
print("Произведение  ",p)

diskrem = s**2 - 4*p
x1 = int(round((s + diskrem**0.5) / 2, 8))
y1 = s - x1
print(f"Загаданные числа это {x1} и {y1}")


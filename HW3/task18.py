# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint

n = int(input("Введите размер массива "))
mass =[randint(1,10) for i in range(n)]
x = int(input("Введите искомое число "))
distanse = abs(mass[0]-x)
dist_index = 0
for j in range(1,n):
    if abs(mass[j] - x) < distanse:
        distanse = abs(mass[j] - x)
        dist_index = j
print(f"ближайшее чисо в этом массиве {mass[dist_index]}")
print(mass)


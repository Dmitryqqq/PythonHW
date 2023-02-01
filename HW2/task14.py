# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N
from random import randint

try:
    n = int(input("Введите чило до которого следует выводить степени 2-х  "))
    count = 1
    num = 1
    while num < n:
        print(num)
        num = 2 ** count
        count+= 1
except:
    print("Введено не корректное число")
exec()
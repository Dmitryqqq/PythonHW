# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint

def Create_List(num):
    list = [0]*num
    for i in range(num):
        list[i] = randint(0,1)
    return list

def Summa(list,x):
    summa = 0
    for i in range(len(list)):
        if list[i] == x: summa +=1
    return(summa)

try:
    n =int(input("Введите число монеток "))    
    if n <= 0:
        n  = n /0

    list1 = Create_List(n)
    print(list1)
    orel = Summa(list1,1)
    if orel > n//2: orel = n-orel
    print("Минимальное количество монет которые нужно перевернуть -- ",orel)
            
except:
    print("Вы ввели не корректные данные")
exit()

# задача 4 НЕГА необязательная Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# НО в условии ошибка ! Этот список для к=9 т.к 0 - это певое число

try:
    k = int(input("Сколько чисел Фибоначчи выводить ?  "))

    x2 = 0
    x1 = 1
    list_Fib = [1,0,1]
    for i in range(2,k):
        list_Fib.append(list_Fib[i] + list_Fib[i-1])
        x1,x2 = x2, x1+x2
    for i in range(k-2):
        list_Fib.insert(0, list_Fib[1] - list_Fib[0])
    print(list_Fib)
except:
    print("Введено не корректное число ")
exec()
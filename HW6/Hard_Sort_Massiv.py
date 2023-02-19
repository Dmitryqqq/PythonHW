# HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов 
# задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint
# import numpy

m = int(input("Введите длину массива : "))
n = int(input("Введите ширину массива : "))

# mass = numpy.array('i',[m,n])
mass = [[randint(1,10)for j in range(m)] for i in range(n)]
mass1 = [[0] * m for i in range(n)]

print(mass)
# print(sorted(mass[0]))

def pr(massiv):
    for i in range(len(massiv)):
        for j in range(len(mass[0])):
            print(massiv[i][j], end =' ')
        print("")    

def sort(massiv):
    ind_x = 0
    ind_y = 0
    maxim = massiv[0][0]
    for i in range(len(massiv)):
        for j in range(len(mass[0])):
            if massiv[i][j] > maxim:
                ind_x = i
                ind_y = j
                maxim = massiv[i][j]
    massiv[ind_x][ind_y] = 0
    return maxim      

pr(mass)

for x in range(len(mass)-1,-1,-1):
        for y in range(len(mass[0])-1,-1,-1):
            z = sort(mass)
           # print(x,y,z)
            mass1[x][y] = z


print()
pr(mass1)


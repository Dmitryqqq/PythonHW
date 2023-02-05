# Задача HARD необязательная Имеется список чисел. 
# Создайте список, в который попадают числа, описывающие 
# максимальную возрастающую последовательность. Порядок 
# элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

mass = [1, 5, 3, 4, 1, 7, 8 , 15 , 1]


# m = mass.Min

minim = mass[0]
maxim = mass[0]
for i in range(len(mass)):
    if minim > mass[i]: minim = mass[i]
    if maxim < mass[i]: maxim = mass[i]

ind=1
min_ind = 1
count =0
count_max =0
for i in range(minim,maxim):
    if i in mass:
        count +=1
        
        if count_max < count: 
            count_max = count
            max_ind = i
            min_ind = ind
    else:
        count =0
        if ind < maxim : ind = i+1
    
otvet = [min_ind,max_ind]

print(mass)
print(otvet)

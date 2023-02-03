# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . 
# Но теперь количество предикатов не три, а генерируется случайным образом 
# от 5 до 25, сами значения предикатов случайные, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа. 
# В конце вывести результат проверки истинности этого утверждения.


import time
from random import randint

time1 = time.time()
moran_teorema = True
for count in range(100):
    n = randint(5,25)
    
    pred = [bool(randint(0,1)) for i in range(n)]
    left_rez = pred.pop()
    right_rez = not left_rez
    
    for i in pred:
        left_rez = left_rez or i
        right_rez = right_rez and not i
    left_rez = not left_rez
    moran_teorema = moran_teorema and left_rez==right_rez

print(f"Время работы {time.time() - time1} сек")
print(f"Теорема Моргана {moran_teorema}")

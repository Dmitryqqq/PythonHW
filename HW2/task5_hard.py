# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в N-мерном пространстве. 
# Сначала задается N с клавиатуры, 
# потом задаются координаты точек.

print()
n = int(input("Введите размерность пространства : "))
koord1=[]
koord2=[]
for i  in range(n):
    print(f"Введите {i+1} координату для первой точки")
    koord1.append(float(input()))
for i  in range(n):
    print(f"Введите {i+1} координату для второй точки")
    koord2.append(float(input()))
summ1 = 0
for i in range(n):
    summ1 = summ1 +(koord2[i]-koord1[i])**2
dist = summ1**0.5
print(f"Дистанция между точками равна {dist}")
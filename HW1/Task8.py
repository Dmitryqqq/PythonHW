# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

try:
    n = int(input("Введите длину шоколадки в дольках "))
    m = int(input("Введите ширину шоколадки в дольках "))
    k = int(input("Сколько долек вы бы хотели отломить ?"))
    if k % n == 0 or k % m == 0:
        print("Да, ломайте")
    else:
        print("Нет, не получится")

except:
    print("Вы ввели не корректные данные")
exit()
# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# сумма цифр любого целолго числа

try:
    n =int(input("Введите целое число "))
    if n < 0:
        n  = n * -1
    summa = 0
    while n > 0:
        x = n % 10
        summa = summa + x
        n = n // 10
    print(summa) 
except:
    print("Вы ввели не корректные данные")
exit()

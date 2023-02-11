# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями 
# вычисления таких выражений нельзя, если только для проверки вашего 
# алгоритма.Hа вход подается строка из операторов / * + - и целых чисел. 
# Надо посчитать результат введенного выражения.
# Например,

# на входе
# 1+9/3*7-4
# на выходе
# 18

# 1+9/3*7-40*7

formula = input("Введите выражение : ")

def formu(formula1):
 # S.isdigit()	Состоит ли строка из цифр    
    if '.' in formula1 and formula1.replace('.', '').isdigit():
        return float(formula1)
    elif formula1[0] == "-" and '.' in formula1[1:] and formula1[1:].replace('.', '').isdigit():
        return float(formula1)
    elif formula1[0] == "-" and formula1[1:].isdigit():
        return int(formula1)
    elif formula1.isdigit():
        return int(formula1)
    
    for i in range(0,len(formula1)-1):
        #print("i цикла * / = ",i)
        if formula1[i] == "/" or formula1[i] == "*":
            print(formula1,"  i_вход * =",i)
            x = i
            while x>0 and (formula1[x-1].isdigit() or formula1[x-1] == "."):
                x=x-1
            z = i
            while z<(len(formula1)-1) and (formula1[z+1].isdigit() or formula1[z+1] == "."):
                z=z+1
            y = float(formula1[i+1:z+1])
            if formula1[i] == "/": y = 1/y
            #print("первый : ",formula1[x:i:1]," второй : ",formula1[i+1:z+1])
            t=float(formula1[x:i])*y
            formula2 = formula1[z+1:]
            formula1 = formula1[:x]+str(t)+formula2
           
            #print(formula1,"  i_завершение=",i)
            return 1*formu(formula1)

    for i in range(0,len(formula1)-1): 
       # print("i цикла + -  = ",i)
        if formula1[i] == "+" or formula1[i] == "-":
            if i == 0 : continue
            print(formula1,"  i_вход + =",i)
            x = i
            while x>0 and (formula1[x-1].isdigit() or formula1[x-1] == "."):
                x=x-1
            z = i
            while z<(len(formula1)-1) and (formula1[z+1].isdigit() or formula1[z+1] == "."):
                z=z+1
            y = float(formula1[i+1:z+1])
            if formula1[i] == "-": y = y*-1
         
            #print("первый : ",formula1[x:i:1]," второй : ",formula1[i+1:z+1])
            t=float(formula1[x:i])+y
            formula2 = formula1[z+1:]
            formula1 = formula1[:x]+str(t)+formula2
            
            #print(formula1,"  i_завершение=",i)
            return 1*formu(formula1)


    return 1*formu(formula1)

print(formu(formula))
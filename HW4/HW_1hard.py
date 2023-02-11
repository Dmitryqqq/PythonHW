# В этой задаче мы реализуем алгоритм дешифровки строк, закодированных с помощью одного из самых простых  
# вариантов кодирования длин серий.

# На вход алгоритму подаётся строка, содержащая цифры и символы латинского алфавита. 
# Эта строка разбивается на так называемые "серии", которые кодируются парой число-символ 
# или просто символ (в таком случае число считается равным единице). Результат должен содержать 
# эти серии в том же порядке, что они и встречаются в исходной строке, при этом каждая серия 
# раскрывается в последовательность символов соответствующей длины. 

# Например, рассмотрим строку  

# 3ab4c2CaB
# Разобъём её на серии
# 3a b 4c 2C a B
# После чего преобразуем серии и получим исходную закодированную строку:
# aaabccccCCaB

vvod = input("Введите данные ")
key = input("Если сжимаем введите 's' если распаковываем 'd'")

def shifr(dann):
    dann1 = []
    count = 1
    for i in range(len(dann)-1):

        if dann[i] == dann[i+1]:
            count += 1
        elif count == 1:
            dann1.append(dann[i])
           
        else:
            dann1.append(str(count)+dann[i])
            count = 1
        if i == (len(dann)-2) and dann[i] != dann[i+1]: 
            dann1.append(dann[i+1])
        
    dann2 = "".join(dann1)        
            
    return dann2

def deshifr (dann):
    dann1 = str()
    num = 1
    nums = ""

    for i in range(len(dann)):
        if dann[i].isnumeric() :
            nums = nums + dann[i]  # собираем двух,трех,... значн числа
        else:
            if nums != "":
                num = int(nums)
                nums = ""
            dann1 = dann1 + dann[i]*num
            num = 1
                        
    return dann1

print(vvod)
if key == 's':
    print(shifr(vvod))
elif key == 'd':
    print(deshifr(vvod))
else:print("Чего вы хотели ? ")
import json

#BD=[12345,True,"яблоко",{"Миша": [898981646,464654654] }]
telBD = [{"name": "python", "surname": "петр", "secondname": "петрович", "telefon": "213213213","points": 10}, {"name": "java", "surname": "иван", "secondname": "коляныч", "telefon": "111222333", 'points': 8}]
base = ["name","surname","secondname","telefon"]  # Обязательная структура базы данных
#print(type(telBD[0].keys()))
def load():
                # загрузить из json
                fname='BD.json' #открываем файл
                with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                    telBD = json.load(fh)  # загружаем из файла данные в словарь telBD
                print('БД успещно загружена')
                #print(telBD)
                return telBD

def save():
            # сохранить в json
            with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(telBD , ensure_ascii=False))  # преобразовываем словарь telBD в unicode-строку и записываем в файл
            print('БД успещно сохранена')
def add():
    new_rec = {}
    for k in base:
        new_rec[k] = input(f"Введите {k} : ")
    return new_rec
#save()
#BDnew = load ()
#print(BDnew)
while True:
    print("/load - Загрузка дазы данных ")
    print("/save - Сохранение базы данных ")
    print("/add - добавление записей ")
    print("/show - показать имеющуюся базу ")
    print("/search - поиск по  базе ")
    print("/exit - выход из программы ")
    command = input("Введите комманду ")
    
    if command =="/load":
        telBD = load()
    elif command == "/save":
        save()

    elif command == "/add":  # добавлене записей
        new_rec = add()
        # new_rec = {}
        # new_rec["name"] = input("Введте имя ")
        # new_rec["surname"] = input("Введте фамилию ")
        # new_rec["secondname"] = input("Введте отчество ")
        # new_rec["telefon"] = input("Введте телефон ")
        telBD.append(new_rec)
    elif command == "/search":
        for k in base:
            print(k)
        serch = input("Что вас интересует ? ")
        data = str(input("Введте искомые данные "))
        res = list(filter(lambda x : x[serch] == data, telBD))
        index = telBD.index(res[0])
        print(f"index = {index}")

        #res = filter(lambda x : x[serch] == data, telBD)
        print (res)
        i = input("Хотите внести корректровку ? ('y' или 'n') или удалить запись ? 'del' > ")
        if i == 'y' or i =='д':
            for k in res[0].keys():
                print(k)
            serch = input("Что изменяем ? ")
            data = str(input("Введте новые данные "))
            res[0][serch] = data
            print(res[0])




        if i == "del":
            telBD.remove(res[0])
            print("Запись успешно удалена") 



        # else: continue

    elif command == "/show":
        for k in telBD:
            print(k)
    # elif command == "/edit":
    #     for k in telBD:
    elif command == "/exit":
        break
    elif command == "/help":
        print("Используемые комманды : ")
        print("/load - Загрузка дазы данных ")
        print("/save - Сохранение базы данных ")
        print("/add - добавление записей ")
        print("/edit - редактрование записей ")
        print("/show - показать имеющуюся базу ")
        print("/search - поиск по  базе ")
        print("/exit - выход из программы ")
        

    else :
        print("Введена неверная комманда, используйте /help")


# res = list(filter(lambda x : x['name'] == 'python', dict_a))
print(telBD)
for k in telBD:
    print(k)
import easygui
import json

'''
easygui.buttonbox(msg='первая', title='вторая', choices=('Button[1]', 'Button[2]'),
image=None, images=None, default_choice=None, cancel_choice=None)

easygui.buttonbox(msg='', title=' ', choices=('Button[1]', 'Button[2]', 'Button[3]'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)


fname='BD1.json' #открываем файл
with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    telBD = json.load(fh)  # загружаем из файла данные в словарь telBD
print('БД успещно загружена')
                
text1 = telBD
print(type(telBD))
easygui.textbox(msg='открываем', title='textbox ',text = text1, codebox=False, callback=None, run=True)

'''


filename = 'BD1.txt'
f = open(filename, 'r', encoding='utf-8')
content = f.readlines()
f.close()
print(type(content))
easygui.textbox(filename, 'Просмотр файла', content)


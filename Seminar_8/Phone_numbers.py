import json
import re

db_path = 'phone_book.json'
welcome = 'Enter comand: 1 - Show phone book | 2 - Add record | 3 - Search  | 4 - Del record | 5 - Change record | q - Quit\n'
phone_book = {}

def print_book(book):
        for k,v in book.items():
                print(k, ' - ', end=" ")
                for i, j in v.items():
                    print(i,":",j, end=" | ")
                print()

def save_db(path, db):
       with open(path, 'w', encoding='utf-8') as fh:
              fh.write(json.dumps(db,ensure_ascii=False))
              print('БД успешно сохранена')

def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local

def new_record(book):
    k=input('Введите имя контакта:')
    a={}
    a['phone']=list(input('Введите номер телефона:').split())
    a['birthday']=input('Введите дату рождения:')
    a['addres']=input('Введите адрес:')
    a['e-mail']=input('Введите e-mail:')
    book[k]=a

def search(book):
    a=input('Put name or number: ')
    for key,value in book.items():
        if re.search(a, key): #a in key:
            print(key,value)
        for j, k in value.items():
             if a in k:
                print(key,value)

def del_record(book):
    user_for_del = input('Who needs to be deleted?\n')
    if user_for_del in book:
        book.pop(user_for_del)
    else:
        print('Данного пользователя нет в БД')

def change_record(book):
    user_for_chan = input('Who needs to be changed?\n')
    what_for_chan = input('What needs to be changed?\n')
    book[user_for_chan][what_for_chan] = input('New information\n')

try:
    phone_book=load_db(db_path)
except:
    phone_book = {
    'Иван Дом' : {'phone': ['79997621456', '79797621400'], 'birthday': '11-11-1989', 'e-mail': 'ivan@mail.ru'},
    'MAX' : {'phone': ['79177621226'], 'addres': 'Moscow'}}
    print('БД не найдена. Создана тестовая БД')

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        new_record(phone_book)
    elif action == '3':
        search(phone_book)
    elif action == '4':
        del_record(phone_book)
    elif action == '5':
        change_record(phone_book)

save_db(db_path, phone_book)

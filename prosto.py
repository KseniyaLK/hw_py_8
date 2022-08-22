# from random import randint
# def f ():
#     result = {}
#     for i in range(5):
#         dict1 = {randint(1,20):'none'}
#         result.update(dict1)
#     return(result)


# print(f())        

dict1 = {
  "1": [
    "Inan",
    "789",
    "castomer"
  ],
  "2": [
    "Sergey",
    "654",
    "povar"
  ]
}

print(dict1["1"][0])


def empl_data(): # сотрудники(id сотрудника, имя сотрудника, личный телефон сотрудника)
    name_empl = input('ВВедите имя сотрудника-> ')
    telephone_empl = input('введите номер телефона сотрудника-> ')
    post = input('ВВедите должность сотрудника-> ')
    data = [name_empl, telephone_empl, post]
    return data

# res = empl_data()

di1 = {}
def new_dict(di1, data):
    if len(di1) == 0:
        id = 1
    else:
        id = max(di1.keys()) + 1
    di1[id] = data

def save_data_js(directory):
    with open ('book.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(directory,ensure_ascii=False))           
        

new_dict(di1, empl_data)
new_dict(di1, empl_data)  
save_data_js(di1)  




#__________________________________________
# Создать информационную систему позволяющую работать 
# с сотрудниками некой компании 
# структура: создать несколько таблиц для выгрузки каждой 
# в отдельный файл json: ключ будет id сотрудника;
# 1. id - фио, телефон
# 2. id - отделы в компании
# 3. id - должности
# 4. id - какой сотрудник на какой должности работает
# !!!! определить в каком отделе работает сотрудник!!!!

import json

def empl_data(): # сотрудники(id сотрудника, имя сотрудника, личный телефон сотрудника)
    id = input ('введите id сотрудника -> ')
    name_empl = input('ВВедите имя сотрудника-> ')
    telephone_empl = input('введите номер телефона сотрудника-> ')
    post = input('ВВедите должность сотрудника-> ')
    data = [name_empl, telephone_empl, post]
    name_id = {}
    name_id[id] = data
    return name_id

res = empl_data()





# def department_data(): # отделы (id отдела, название отдела, должности отдела, телефон отдела)
#     id = input ('введите id отдела ->')
#     name_department = input('ВВедите название отдела-> ')
#     post_dapertment = input('введите должности отдеда -> ')
#     telephone_department = input('введите номер телефона отдела-> ')
#     data = [name_department, telephone_department]
#     name_id = {}
#     name_id[id] = data
#     return name_id



# def post_data(): # должность сотрудника (id сотрудника, должность сотрудника)
    # id = input ('введите id сотрудника -> ')
    # post = input('ВВедите должность сотрудника-> ')
    # data = [post]
    # post_id = {}
    # post_id[id] = data
    # return post_id

   


# def unification_data (di1, di2): #сложение словарей по ключам (при их совпадении)
#     di3 = di1
#     for key, value in di2.items():
#         if key in di1:
#             di3[key] += value
#         else:
#             # di3.update({key: value})
#             print('вы ввели неверный id сотрудника')
#     return di3

# res = unification_data(empl_data(), post_data())
# print(res) 


# ________________JSON____________________
def save_data_js():
    with open ('book.json', 'a', encoding='utf-8') as empl_book:
        json.dump(res, empl_book, indent = 2, ensure_ascii=False)           
        print('данные успешно сохранены')

def load_data_js():
     with open ('book.json', 'r', encoding='utf-8') as empl_book:
        book_data = json.load(empl_book)
        print (book_data)


# save_data_js()    
# load_data_js()
 
   

# ________________TXT____________________
# def convert_data_txt():
#     vvod()
#     data = (telephone, comment)
#     book = {}
#     book[name] = data
#     return str(book)

# def save_data_txt():
#     with open ('book.txt', 'a', encoding='utf-8') as empl_book:
#         empl_book.write(f'{str(res)}\n')

# def load_data_txt():
#      with open ('book.txt', 'r', encoding='utf-8') as empl_book:
#         book_data = empl_book.read()
#         return(book_data)

# save_data_txt()
# print(load_data_txt())        


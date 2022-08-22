
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




 
   

  






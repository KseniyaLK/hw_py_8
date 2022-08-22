import data 
import view


#метод нажатия на кнопку
def button_click():
    print('Вас приветсвует БД сотрудников компании!\nВыберите необходимый пункт меню: ')
    print('1. Добавление сотрудника компании')
    # print('2. Удаление сотрудника компании')
    print('3. Импорт данных')
    print('4. Экспорт данных')
    print('5. Выход из БД')

    status = False
    while status == False:
        k = input('введите пункт меню: ')
        if  k == '1':
            result = {}
            result.update(dict(data.empl_data()))
            view.view_data(result)# возврат значения в view
            status = False 
            
        elif k == '3':  
            result = data.save_data_js()
            view.view_data(result)# возврат значения в view
            status = False
            # break
        elif k == '4':  
            result = data.load_data_js()
            view.view_data(result)# возврат значения в view
            status = False
            # break
        elif k == '5':  
            break
        else:    
            print ('Некорректный ввод. Введите число от 1 до 5')
    return result    
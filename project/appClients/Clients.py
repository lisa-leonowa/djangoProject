import json


def get_values(valid_form):  # получение значений из формы
    if valid_form.is_valid():  # если форма была отправлена
        value = []  # массив для хранения значений формы
        for i in valid_form.form_values():  # переборка значений
            value.append(valid_form.cleaned_data[i])  # добавления значения в массив
        return value  # возврат массива с данными
    return "Invalied Data"  # сообщение об ошибке

def add_client(list_values_form):  # добавление клиента в файл
    phone = list_values_form[4]  # номер телефона выступает ключом
    if not chek_client(phone):  # если такого клиента нет, то добавляем
        with open('appClients/Clients.json', encoding='utf-8') as f:
            data = json.load(f)
        print('----------------------------------------------------------------------------------------------------')
        last_id = int(sorted(data.keys())[-1])
        data[str(last_id+1)] = {
            "first_name": list_values_form[0],
            "last_name": list_values_form[1],
            "full_name": list_values_form[2],
            "phone": phone,
            "gender": list_values_form[3],
            "remark": list_values_form[5],
            "services": []
        }
        with open('appClients/Clients.json', 'w', encoding='utf-8') as f:
            json.dump(data, ensure_ascii=False, fp=f, indent=4)
        return True
    return 0  # если такой клиент есть, добавление не будет выполнено

def update_client(list_values_form):  # добавление клиента в файл
    phone = list_values_form[0]  # номер телефона выступает ключом
    if chek_client(phone):  # если такой клиент есть
        with open('appClients/Clients.json', encoding='utf-8') as f:
            data = json.load(f)
        data[phone]['remark'] = list_values_form[1]
        with open('appClients/Clients.json', 'w', encoding='utf-8') as f:
            json.dump(data, ensure_ascii=False, fp=f, indent=4)
        return True
    return False

def chek_client(phone):  # наличие клиента в списках
    with open('appClients/Clients.json', encoding='utf-8') as f:
        data = json.load(f)
    try:
        if data[phone]:
            return True  # клиент есть в базе
    except:
        return False  # клиента нет в базе

def select_clients():
    with open('appClients/Clients.json', encoding='utf-8') as f:
        data = json.load(f)
    return data

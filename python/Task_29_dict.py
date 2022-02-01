# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

def change_dict(d):
   # d = {1: 10, 2: 20, 3: 30}
    print(d)
    print(id(d))
    list_key = []
    list_value = []
    for el in d.keys():
        list_key.append(el)
    for el in d.values():
        list_value.append(el)
    list_key.remove(list_key[1])
    list_value.remove(list_value[1])
    print(list_key)
    list_key[0], list_key[-1] = list_key[-1], list_key[0]
    print(list_key)
    print(list_value)
    d.clear()
    #for el in list_key:
    index = 0
    while index <= len(list_key) - 1:
        d[list_key[index]] = list_value[index]
        index += 1
    d['«new_key»'] = '«new_value»'
    print(d)
    print(id(d))
   
if __name__ == '__main__':
    my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    change_dict(my_dict)

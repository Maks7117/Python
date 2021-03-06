# Получите первый и последний элемент списка
# Проверить, есть ли в последовательности дубликаты

def first_last(lst):
    print(lst[0])
    print(lst[-1])

def copy_in_list(lst):
    la = list(lst)
    new_list = []
    index = 0
    while len(la) != 0:
        for el in la:
            x = el
            la.remove(el)
            if x in la:
                print(el)



if __name__ == '__main__':
    l = [1, 2, 3, 5, 2, 5, 4, 5, 1.2, 1.2]
    first_last(l)
    copy_in_list(l)
    # Создаем список с дубликатами lst
    lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]

    # На основе списка создаем множество st
    # Помним про основное свойство множеств - они не могут содержать дубликатов
    # Поэтому если lst содержит дубликаты, то при создании множества на его основе дубликаты будут удалены
    st = set(lst)

    # А значит количество элементов в списке и во множестве будет различаться
    # Сравниваем количество элементов с помощью встроенного метода len()
    len(st) == len(lst)
    False
    # Длины не равны, значит в изначальном списке были дубликаты
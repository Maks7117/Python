#1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка

def list_example():
    lst = []
    for el in range(0, 10):
        lst.append(el)
    print(lst)
    lst.append('sds')
    lst.insert(5, 8)
    l = ['dssd', 2, 'wds']
    lst.append(['a', 'b', 'a', 'hello'])
    t = tuple('hello')
    lst.insert(3, t)
    lst[4] = 189
    lst.append(l)
    res = lst[8]
    lst.remove(9)
    lst.pop(3)
    print(res)
    print(lst)

def count_repeat(x):
    index = 0
    count = 0
    super_number = 0
    print(x.count(5))
    while index <= len(x) - 1:
        repeat = 0
        number = 0
        for el in x:
            if x[index] == el:
                repeat = repeat + 1
                number = el
                if repeat > count:
                    count = repeat
                    super_number = number
        index = index + 1
    print('number - ' + str(super_number) + ' / repeat -' + str(count) + ' times')
if __name__ == '__main__':
    ls = [1, 1, 22, 22, 3, 22, 5, 22, 5, 5, 5, 5, 5, 5]

    #list_example()
    count_repeat(ls)

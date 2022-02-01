# Перед студентом стоит задача:
# на вход функции sieve() поступает список целых чисел.
# В результате выполнения этой функции
# будет получен кортеж уникальных элементов списка в обратном порядке.

def sieve(lst):
    index = len(lst) - 1
    new_list = []
    while index >= 0:
        if lst[index] not in new_list:
            new_list.append(lst[index])
        index -= 1
    #for el in new_list:
    return print(tuple(new_list))

def sieve_magic(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)

if __name__ == '__main__':
    l = [1, 3, 5, 3, 4, 1, 1, 5, 3]
    ss = [1, 2, 3, 2, 4]
    sieve(l)
    sieve_magic(l)


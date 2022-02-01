#Напишите программу для слияния нескольких словарей в один
def dict_add(a, b, c):
    new_dict = {**a, **b, **c}
    return print(new_dict)
def dict_add_2(a, b, c,):
    new_dict = {}
    for el in (a, b, c):
        new_dict.update(el)
    return print(new_dict)


if __name__ == '__main__':
    dict_add_2({1: 3, 2: 43}, {44: 22, 'a': 122}, {'qq': 55, 2222: 'wewew'})
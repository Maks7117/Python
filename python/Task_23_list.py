# Напишите функцию change(lst),
# которая принимает список и меняет местами его первый и последний элемент
# В исходном списке минимум 2 элемента

def change_list(lst):
    a, b = lst[0], lst[-1]
    lst[0], lst[-1] = b, a
    print(lst)
    print(max(lst))


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    change_list(l)
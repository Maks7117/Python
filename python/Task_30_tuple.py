# Напишите функцию tpl_sort(), которая сортирует кортеж,
# состоящий из целых чисел по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом,
# то функция возвращает исходный кортеж.

def tpl_sort():
    tpl = tuple([1, 2, 4, 53, 5])

    for el in tpl:
        if not isinstance(el, int):
            return print(tpl)

    return print(tuple(sorted(tpl)))

if __name__ == '__main__':
    tpl_sort()
# Функция slicer() на вход принимает кортеж и случайный элемент.
# Требуется вернуть новый кортеж,
# начинающийся с первого появления элемента в нем
# и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз,
# то вернуть кортеж, который начинается с него и идет до конца исходного.

def slicer(tpl, x):
    if tpl.count(x) >= 2:
        first = tpl.index(x, 0)
        second = tpl.index(x, first + 1)
        new_tuple = tpl[first:second + 1]
        print(new_tuple)
    elif tpl.count(x) == 1:
        first = tpl.index(x, 0)
        new_tuple = tpl[first:]
        print(new_tuple)
    elif tpl.count(x) == 0:
        new_tuple = tuple()
        print(new_tuple)

if __name__ == '__main__':
    t = tuple([1, 2, 33, 1, 2, 71, 3, 33, 89])
    slicer(t, 33)
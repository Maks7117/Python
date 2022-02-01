# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst),
# которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной,
# дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.

def all_eg(s):
    new_lst = []
    index = 0
    max = ''
    while index <= len(s) - 1:
        for el in s:
            if len(el) > len(max):
                max = el
        index += 1
    for el in s:
        while len(el) < len(max):
            el = el + '_'
        new_lst.append(el)
    print(new_lst)


if __name__ == '__main__':
    l = ['my name', 'buy a car', 'where are you from', 'car', 'given']
    x = ['a', 'aaa', 'aaaa', 'dd']
    all_eg(x)
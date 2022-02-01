# На основании предоставленного отрывка текста
# определить 3 наиболее часто встречаемых символа в ней.
# Пробелы нужно игнорировать (не учитывать при подсчете).
# Для выведения результатов вычислений требуется написать функцию top3(st).
# Итог работы функции представить в виде строки:
# «символ – количество раз, символ – количество раз…».

from collections import Counter

def top3(st):
    lst = []
    dct = dict()
    for el in st:
        index = 0
        count = 0
        while index <= len(st) - 1:
            if el == ' ':
                st.replace(' ', '')
            elif el == st[index]:
                count += 1
                dct[el] = count
            index += 1
    print(dct)
    #for value in dct.values():
       # lst.append(value)
       # lst = sorted(lst, reverse=True)
    lst_values = sorted(list(dct.values()), reverse=True)
    print(lst_values)
    lst_keys = sorted(list(dct.keys()), reverse=True)
    print(lst_keys)
    i = 0
    new_dct = {}
    while i <= len(lst_values) - 1:
        new_dct[lst_values[i]] = lst_keys[i]
        i = i + 1
    print(new_dct)


def top3_magic(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

if __name__ == '__main__':
    s = 'efdefdf frerfdf ef'
    top3(s)
    print(top3_magic(s))


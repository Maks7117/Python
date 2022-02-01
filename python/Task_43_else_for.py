# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа,
# которые больше 5 по модулю.

def more_than_five(lst):
    l = []
    for el in lst:
        if el > 5:
            l.append(el)
    return print(l)

if __name__ == '__main__':
    more_than_five([1, 4, 54, 5, 47, 4, 5, 74, 1, 7])
    letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'

    for letter in letters:
        if letter == letter.upper():
            letters = letters.replace(letter, '')


    print(letters)
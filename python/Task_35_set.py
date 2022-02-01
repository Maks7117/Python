# На входе функция to_set() получает строку или список чисел.
# Преобразуйте их в множество.
# На выходе должно получиться множество и его мощность.

def to_set(x):
    st = set(x)
    return st, 'Мощночть = ' + str(len(st))

if __name__ == '__main__':
    string = "Hello friend hello"
    lst = [1, 2, 3, 1]

    print(to_set(lst))
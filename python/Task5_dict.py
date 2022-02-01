#Найдите три ключа с самыми высокими значениями в словаре
#my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
import operator


def sort_dict(a):
    res = sorted(a, key=a.get, reverse=True)[:3]
    print(a)
    print(res)
    print(type(res))
    print(type(a))


if __name__ == '__main__':
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    sort_dict(my_dict)
    print(int('ABC', 16))
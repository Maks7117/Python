#Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator


def task_3(a):
    result = dict(sorted(a.items(), key=operator.itemgetter(1)))
    result2 = dict(sorted(a.items(), key=operator.itemgetter(1), reverse=True))
    print(result)
    print(result2)

def sort_dict(a):
    list_keys_a = list(a.keys())
    list_keys_a.sort()
    for el in list_keys_a:
        print(el)

if __name__ == '__main__':
    d = {'a': 10, 'b': 15, 'c': 4}
    task_3({1: 5, 2: 32, 'a': 21})
    #sort_dict(d)
    #print(d.items())

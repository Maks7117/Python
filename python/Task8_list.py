#Выведите первый и последний элемент списка

def print_list(input):
    lst = list(input)
    print(lst[0])
    print(lst[len(lst) - 1])

if __name__ == '__main__':
    l = [1, 2, 2, 2, 3]
    print_list(l)

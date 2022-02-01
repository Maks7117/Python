# Требуется создать функцию list_sort(lst),
# которая сортирует список чисел по убыванию их абсолютного значения

def list_sort(lst):
    lst.sort(reverse=True)
    print(lst)

def sort_bubble(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                buff = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = buff

    print(lst)
if __name__ == '__main__':
    l = [3, 4, 2, 111, 23, 5, 43, 21, 101]
    list_sort(l)
    sort_bubble(l)

# Дан произвольный список.
# Представьте его в обратном порядке.

def revers_list(lst):
    index = len(lst) - 1
    while index >= 0:
        print(lst[index])
        index = index - 1

def revers_list_2(my_list):
    print(my_list[::-1])

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    revers_list(l)
    revers_list_2(l)
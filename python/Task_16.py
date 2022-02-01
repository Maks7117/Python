#Нужно проверить, все ли числа в последовательности уникальны


def unique(lst):
    las = list(lst)
    while len(las) != 0:
        #print(str(lst) + ' do for')
        for el in las:
            x = el
            las.remove(el)
            #print(str(lst) + ' posle for')
            if x in las:
                print(str(las) + ' posle if')
                return False
    return True

def all_unique(numbers):
    return len(numbers) == len(set(numbers))

def div_on_15(lst):
    new_list = []
    for el in lst:
        if el % 15 == 0:
            new_list.append(el)
            print(el)
    for el in new_list:
        print('new_list[el] = ' + str(el))
    print(new_list)

if __name__ == '__main__':
    l = [25, 2, 27, 258, 3, 30, 2589, 258]

    #print(all_unique(l))
    print(unique(l))
    div_on_15(l)
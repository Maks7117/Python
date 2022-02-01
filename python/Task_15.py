#С помощью анонимной функции извлеките из списка числа, делимые на 15

def div_on_15(lst):
    new_list = []
    for el in lst:
        if el % 15 == 0:
            new_list.append(el)
            print(el)
    for el in new_list:
        print('new_list[el] = ' + str(el))
    print(new_list)

def div_variant_2(lst):
    result = list(filter(lambda x: not x % 15, lst))
    print('result_variant_2 =' + str(result))
    print(type(result))
if __name__ == '__main__':
    l = [11, 74, 15, 45, 60, 58, 685, 64, 8]
    div_on_15(l)
    div_variant_2(l)
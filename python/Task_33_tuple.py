# Николай знает, что кортежи являются неизменяемыми, но он с этим не готов соглашаться.
# Ученик решил создать функцию del_from_tuple(),
# которая будет удалять первое появление определенного элемента
# из кортежа по значению и возвращать кортеж без оного.
# Попробуйте повторить шедевр не признающего авторитеты начинающего программиста.
# К слову, Николай не всегда уверен в наличии элемента в кортеже
# (в этом случае кортеж вернется функцией в исходном виде).

def del_from_tuple(tpl, x):
    lst = list(tpl)
    if x in lst:
        lst.remove(x)
        print(tuple(lst))
    else:
        print(tpl)
        

def del_from_tuple_magic(tpl, elem):
    if elem in tpl:
        elem_index = tpl.index(elem)
        return tpl[:elem_index] + tpl[elem_index + 1:]
    return tpl


if __name__ == '__main__':
    my_tpl = tuple([1, 2, 3, 4])
    del_from_tuple(my_tpl, 3)
    print(del_from_tuple_magic(my_tpl, 3))


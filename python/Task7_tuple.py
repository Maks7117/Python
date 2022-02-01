#Вы принимаете от пользователя последовательность чисел, разделённых запятой
#Составьте список и кортеж с этими числами

def list_tuple(string):
    list_input = list(string)
    new_list = []
    for el in list_input:
        if el != ',':
            new_list.append(int(el))
            #list_input.remove(el)
        #else:
            #list_input.append(el)
    tuple_input = tuple(new_list)
    print(new_list)
    print(tuple_input)





if __name__ == '__main__':
    c = input()
    list_tuple(c)
    a = tuple('hello, word')
    aa = ('hello,. bob!')


    c = list('go ggo')
    cc = ['sss dd, ds']

    s = dict([('dss', 1), (2, 'dssd')])
    ss = {2: 323, 'f': 'dds'}

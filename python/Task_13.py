#Посчитайте, сколько раз символ встречается в строке

def symbol_count(str, a):
    count = 0
    index = 0
    while index <= len(str) - 1:
        if str[index] == a:
            count += 1
        index += 1
    print(count)

def count(str, b):
    print(str.count(b))

if __name__ == '__main__':
    symbol_count('aaavv tr eraaaaaaaaaaaaa', 'a')
    count('dfdsfdvd thtgfhf yujrdf d', 'f')
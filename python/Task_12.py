#Сложите цифры целого числа

def add(a):
    a = str(a)
    res = 0
    index = 0
    while index <= len(a) - 1:
        res = int(a[index]) + res
        index = index + 1
    print(res)

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    print(sum(digits))


if __name__ == '__main__':
    add(145)
    sum_digits(458)
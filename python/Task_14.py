#Поменяйте значения переменных местами

def task_14(a, b):
    a, b = b, a
    print(str(a) + '=' ' a')
    print(str(b) + '=' ' b')

def task_2_variant_2(x, y):
    temp = x
    x = y
    y = temp
    print(str(x) + '=' ' x')
    print(str(y) + '=' ' y')

if __name__ == '__main__':
    a = 12
    b = 45
    task_14(a, b)
    x = 5
    y = 10
    task_2_variant_2(x, y)

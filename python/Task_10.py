#При заданном целом числе n посчитайте n + nn + nnn

def mul_n(n):
    result = n + (n * n) + (n * n * n)
    print(result)

if __name__ == '__main__':
    mul_n(2)
# Напишите функцию dislike_6(a), которая всегда возвращает True,
# если только не передается число 6 типа int
# или типа float (в данном случае она вернет «Только не 6!»)

def dislike_6(a):
    if (type(a) is int or type(a) is float) and a == 6:
        return "tolko ne 6!"
    return True
if __name__ == '__main__':
    print(dislike_6(5+1.0))
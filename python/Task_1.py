def task_1(array):
    for elem in array:
        if elem < 5 or elem > 21:
            print(elem)

if __name__ == '__main__':
    task_1([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

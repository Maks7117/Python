# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    if (month <= 2) or (month == 12):
        print('winter')
    elif (month >= 2) and (month <= 5):
        print('spring')
    elif (month >= 6) and (month <= 8):
        print('summer')
    elif (month >= 7) and (month <= 11):
        print('autumn')

if __name__ == '__main__':
    season(9)
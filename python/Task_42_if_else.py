# Число делится на 6 только в случае соблюдения двух условий:
# последняя его цифра четная, а сумма всех цифр делится на 3.
# Напишите функцию is_divisible_by_6(number),
# которая возвращает «Число Х делится на 6» или «Число Х неделимо на 6»
# в зависимости от того, можно ли его разделить на 6.
# В качестве аргумента может быть передано любое целое число.

def is_divisible_by_6(number):
    x = str(number)
    index = 0
    sum = 0
    while index <= len(x) - 1:
        sum = sum + int(x[index])
        last_number = int(x[len(x) - 1])
        index += 1

    if last_number % 2 == 0 and sum % 3 == 0:
        return '«Число Х делится на 6»'
    else:
        return '«Число Х неделимо на 6»'

if __name__ == '__main__':
    print(is_divisible_by_6(1125481))
# Требуется определить индексы первого
# и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st),
# включающую 2 параметра: letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None),
# если же она есть, то кортеж будет состоять из первого
# и последнего индекса этого символа.

def first_last(st, letter):

    first = st.find(letter)
    last = st.rfind(letter)
    if first < 0:
        return None, None
    return first, last

if __name__ == '__main__':
    st = "Hello my friend and world"
    print(first_last(st, 'l'))
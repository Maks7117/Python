# Александр решил как-то отобразить в тексте
# BACKSPACE (т.е. удаление последнего символа).
# Он подумал, что символ «@» отлично для этого подходит.
# Всем своим знакомым он дал строки
# такого вида (например, «гр@оо@лк@оц@ва»),
# чтобы посмотреть, кому удастся написать функцию cleaned_str(st),
# возвращающую строку в ее чистом виде.

def cleaned_str(st):
    text = ''
    for el in st:
        if el == '@':
            st = st.replace(el, '')
        else:
            text = text + el
    print(st)

def cleaned_str_magic(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)


if __name__ == '__main__':
    s = 'сварка@@@@@лоб@ну@'
    s2 = 'гр@оо@лк@оц@ва'
    cleaned_str(s2)
    print(cleaned_str_magic(s2))
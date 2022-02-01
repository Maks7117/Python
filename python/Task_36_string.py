# Напишите функцию search_substr(subst, st),
# которая принимает 2 строки и определяет,
# имеется ли подстрока subst в строке st.
# В случае нахождения подстроки,
# возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

def earch_substr(subst, st):
    if subst.lower() in st.lower():
        return '«Есть контакт!»'
    else:
        return '«Мимо!»'

if __name__ == '__main__':
    st = 'Hello my friend and world'
    subst = "FRie"
    print(earch_substr(subst, st))

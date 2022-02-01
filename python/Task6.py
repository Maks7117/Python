#Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.



def palinrom(string):
    index = 0
    text = ''
    while index <= len(string) - 1:
        text = string[index] + text
        index = index + 1
    if text == string:
        print(text)
        return True
    else:
        print(text)
        return False
if __name__ == '__main__':
    print(palinrom('а путана тупа'))
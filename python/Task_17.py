# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное
import re

def print_word(str):
    max = ''
    count = 0
    s = []
    s = str.split(' ')
    for el in s:
        if len(max) < len(el):
            max = el
    print(s)
    print(max)
    index = 0
    super_max = 0
    w = ''
    while index <= len(s) - 1:
        word_max = 0
        for el in s:
            if s[index] == el:
                word_max = word_max + 1
                if word_max > super_max:
                    super_max = word_max
        index = index + 1
    print(word_max)

def max_number(lst):
    max = 0
    for el in lst:
        if max < el:
            max = el
    print(max)

if __name__ == '__main__':
    t = 'is isss is'
    print_word(t)
    l = [1, 3, 321, 4, 2, 33, 2]

    #max_number(l)
# -*- coding: utf-8 -*-
"""
@author: unknown

ProjectEuler-problem-42
"""

def get_word_values(word):
    """ 单词的值 """
    return sum([ord(w) - ord('A') + 1 for w in word])


def is_tn(y):
    """ 三角形单词 """
    x = (-1 + pow(1 + 8 * y, 0.5)) / 2
    if int(x) == x:
        return True
    else:
        return False


all_word = open(r'f:/content/ProjectEuler/data/42.txt','r').read()
word_list = all_word.replace('"', '').split(',')

n = 0
for word in word_list:
    if is_tn(get_word_values(word)):
        n += 1
print(n)
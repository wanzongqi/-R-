# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-22
"""

name_str = open(r'f:/content/ProjectEuler/data/22.txt').read()
name_str = name_str.replace('"', '')
name_list = name_str.split(',')
name_list.sort() #对字符串可以直接按照字母表排序了
score_sum = 0
for i,name in enumerate(name_list):
    score = (i + 1) * sum([ord(n) - 64 for n in name])
    score_sum += score
print(score_sum)
        

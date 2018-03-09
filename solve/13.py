# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-13
"""

"""
本意是高精度计算，用字符串以及竖式，但是python可以支持50位数字的计算
"""

sum = 0
f = open(r'f://content/ProjectEuler/data/13.txt','r')
for i in range(100):
    sum = sum + int(f.readline())
print(sum)
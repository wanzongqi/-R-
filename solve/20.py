# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-20
"""
n = 1
for i in range(100):
    n = n*(i+1)

str_n = str(n)
sum = 0
for i in str_n:
    sum = sum+int(i)
print(sum)
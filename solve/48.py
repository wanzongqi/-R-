# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-41
"""
summ = 0
for i in range(1,1001):
    multim = 1
    for j in range(i):
        multim *= i
        multim = multim%10000000000
    summ += multim
    summ = summ%10000000000
    
print(summ)
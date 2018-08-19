# -*- coding: utf-8 -*-
"""
pe-65

@author: strA
"""

a = []
for i in range(100):
    if i%3==2:
        a.append(2*(i//3+1))
    else:
        a.append(1)
a[0] = 2

a = reversed(a)
numerator = 0
dinomitor = 1
for x in a:
    numerator = numerator + x*dinomitor
    temp = dinomitor
    dinomitor = numerator
    numerator = temp
#最后一次也翻转了，所以应该是分母
print(dinomitor)
num = 0
for c in str(dinomitor):
    num += int(c)
print(num)
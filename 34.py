# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-34
"""

factorial = [1,1,2,6,24,120,720,5040,40320,362880]
max = 2110000
def handle(n):
    n = str(n)
    sum = 0
    for dig in n:
        sum += factorial[int(dig)]
    return sum

sum=0
for i in range(1,max):
    if handle(i)==i:
        sum+=i
        print(i)
print(sum-3)
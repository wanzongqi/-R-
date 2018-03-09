# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-21
"""
import math
d = [0]*10001
def sod(n):
    sum = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sum = sum+i+int(n/i)
    if math.sqrt(n)-int(math.sqrt(n))<0.001:
        sum = sum-int(math.sqrt(n))
    return sum

for i in range(2,10001):
    d[i] = sod(i)

amicable = []

for i in range(2,10001):
    if (d[i]<10001) and (d[d[i]] == i) and (d[i] != i):
        amicable.append(i)

sum = 0
for i in amicable:
    sum = sum + i
print(sum)
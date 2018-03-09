# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-12
"""

import math

def factor_count(n):
    t = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            t += 1
    t = 2*t
    if math.sqrt(n) - int(math.sqrt(n))<0.001:
        t = t-1
    return t

sum = 1
term = 1
while factor_count(sum)<=500:
    term += 1
    sum = sum+term
print(sum)
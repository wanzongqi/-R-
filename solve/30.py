# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-30
"""

def sodigits(n):
    s = 0
    while n > 0:
        s = s+(n%10)**5
        n = n//10
    return s

sum = 0
for i in range(1,354295):
    if sodigits(i) == i:
       sum += i
print(sum-1)
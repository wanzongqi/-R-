# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-45
"""
import math

def T(n):
    return n*(n+1)/2

def is_H(n):
    return int((1+math.sqrt(1+8*n))/4)==(1+math.sqrt(1+8*n))/4

def is_P(n):
    return int((1+math.sqrt(1+24*n))/6)==(1+math.sqrt(1+24*n))/6

n = 286
while True:
    t = T(n)
    if is_H(t) and is_P(t):
        print(t)
        break
    n += 1
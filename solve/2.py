# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-2
"""

a = 1
b = 1
c = a+b
sum = 0
while c<4000000:
    sum = sum + c
    a = b
    b = c
    c = a+b
    a = b
    b = c
    c = a+b
    a = b
    b = c
    c = a+b
    
print(sum)
    
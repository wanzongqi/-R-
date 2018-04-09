# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:55:21 2018

@author: dell
"""

numerator = 1
denominator = 1

def change(a,b):
    t = a
    a = b
    b = t
    return a,b

count = 0
for i in range(1000):
    numerator += denominator
    numerator,denominator = change(numerator,denominator)
    numerator += denominator
    if len(str(numerator))>len(str(denominator)):
        count+=1
print(count)
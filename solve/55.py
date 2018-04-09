# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:48:53 2018

@author: dell
"""
max_s = 0
for a in range(1,100):
    for b in range(1,100):
        n = str(a**b)
        s = 0
        for i in range(len(n)):
            s += int(n[i])
        if s>max_s:
            max_s=s
print(max_s)
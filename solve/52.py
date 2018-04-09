# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:44:15 2018

@author: dell
"""
n = 10000
while True:
    if n%2000==0:
        print(n)
    l = [sorted(list(str(i*n))) for i in range(1,7)]
    check = [l[i]==l[i+1] for i in range(len(l)-1)].count(True)
    if check==len(l)-1:
        print(n)
        break
    n += 1
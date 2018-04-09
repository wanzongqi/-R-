# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:42:01 2018

@author: dell
"""
answers = []
for i in range(10,10001):
    if i%10==0:
        print(i/10)
    k = 0
    l = i
    while k<50:
        l = l+int(str(l)[::-1])
        if str(l)==str(l)[::-1]:
            break
        k+=1
    if k==50:
        answers.append(i)
print(len(answers))
    
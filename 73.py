# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:47:53 2018
pe-73
@author: strA
"""
p = []
flag = [True]*12001
for i in range(2,12001):
    if flag[i]:
        p.append(i)
        for j in range(2,12000//i+1):
            flag[i*j] = False
def check(p,a,b):
    for pp in p:
        if a%pp==0 and b%pp==0:
            return False
    return True

num = 0
for d in range(3,12001):
    print(d)
    n1 = int((1/2)*d)+1
    n2 = int((2/3)*d)
    for i in range(n1,n2+1):
        if check(p,i,d):
            num += 1
print(num-1)
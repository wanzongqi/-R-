# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-14
"""

"""
给出角谷猜想对100万以下数的证明
"""

term = [0]*1000001
term[1] = 1
max = 1
maxnum = 1
def c_next(n):
    if n%2==0:
        return int(n/2)
    else:
        return 3*n+1

for i in range(2,1000001):
    t = 1
    k = i
    while c_next(k)>1:
        k = c_next(k)
        t += 1
    if t>max:
        max = t
        maxnum = i

print(max,maxnum)
    
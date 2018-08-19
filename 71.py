# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:43:50 2018
pe-71
@author: strA
"""
def frac_max(n1,d1,n2,d2):
    #第一个分数是否比第二个大
    if n1*d2-n2*d1>0:
        return True
    return False
d_min_n = 0
d_min_d = 1
for n in range(8,1000001):
    if n%7==0:
        continue
    m = int((3/7)*n)
    if frac_max(m,n,d_min_n,d_min_d):
        d_min_n = m
        d_min_d = n
print(d_min_n)
print(d_min_d)
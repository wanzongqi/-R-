# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:04:17 2018

@author: dell
"""

"""
参见wiki 条目佩尔方程,连分数递推参见条目中定理1,浮点数导致数值灾难，参见64
"""
max_x = 0
for D in range(200,1001):
    print(D)
    if D**(1/2)==int(D**(1/2)):
        continue
    d = D**(1/2)
    p = 0
    q = 1
    a = int(d)
    denominator = [0,1]
    numerator = [1,a]
    while numerator[1]**2-D*denominator[1]**2!=1:
        p = a*q-p
        q = (D-p**2)/q
        a=(int(d)+p)//q
        numerator_n = numerator[0]+a*numerator[1]
        denominator_n =denominator[0]+a*denominator[1]
        denominator = [denominator[1],denominator_n]
        numerator = [numerator[1],numerator_n]
    if numerator[1]>max_x:
        max_x = numerator[1]
        print(max_x,D)
print(max_x,)
        
        
    
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-10
"""

"""
用筛法得到200w以下的素数
"""

prime = [True]*2000001
prime[0] = False
prime[1] = False

for i in range(2000001):
    if prime[i]:
        for j in range(2,int(2000000/i)+1):
            prime[j*i] = False

sum = 0
for i in range(2000001):
    if prime[i]:
        sum = sum + i
print(sum)
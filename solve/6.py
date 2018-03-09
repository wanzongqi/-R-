# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-6
"""

sum = 0
for i in range(1,101):
    for j in range(1,101):
       sum = sum+i*j

for i in range(1,101):
    sum = sum - i*i

print(sum)
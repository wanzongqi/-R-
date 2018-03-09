# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-33
"""

def d_cancell(a,b):
    a = str(a)
    b = str(b)
    if a[1] == '0' and b[1] == '0':
        return 1
    if a[0] == b[0]:
        if int(b[1])==0:
            return 1
        return int(a[1])/int(b[1])
    if a[0] == b[1]:
        if int(b[0])==0:
            return 1
        return int(a[1])/int(b[0])
    if a[1] == b[0]:
        if int(b[1])==0:
            return 1
        return int(a[0])/int(b[1])
    if a[1] == b[1]:
        if int(b[0])==0:
            return 1
        return int(a[0])/int(b[0])
    
multi_n = 1
multi_d = 1
for i in range(10,100):
    for j in range(i+1,100):
        if d_cancell(i,j)==i/j:
            print(i,j)
            multi_n = multi_n*i
            multi_d = multi_d*j
print(multi_n,multi_d)
            
    
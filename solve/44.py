# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-44
"""

"""
先写个简单的
"""
import math
def check(n):
    if int((1+math.sqrt(1+24*n))/6)==(1+math.sqrt(1+24*n))/6:
        return True
    else:
        return False
    
def Pentagon(n):
    return (n*(3*n-1))//2

i = 1
flag = True
while flag:
    j = 1
    while j<i:
        diff = Pentagon(i)-Pentagon(j)
        sum = Pentagon(i)+Pentagon(j)
        if check(diff) and check(sum):
            flag = False
            print(diff)
            break
        j +=1
    i += 1

    
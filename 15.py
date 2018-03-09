# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-15
"""

"""
简单组合题
相当于将20个球放进40个区别开的盒子里有多少方法，即C(40,20)
"""

def jie(n):
    if n == 1:
        return 1
    else:
        return n*jie(n-1)
 
def C(m,n):
    return jie(m)/(jie(n)*jie(m-n))

print(C(40,20))    
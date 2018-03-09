# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-1
"""

def Sum(n,m):
    """
    计算低于n的m的倍数的和
    """
    nn = int((n-1)/m)
    nn = nn*(nn+1)/2
    return nn*m

print(Sum(1000,3)+Sum(1000,5)-Sum(1000,15))
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:25:36 2018

@author: strA
"""

ans = [[0 for j in range(100)] for i in range(101)]
#ans[i][j]代表用不超过j的数加到i的方案数
ans[1] = [1]*100
for i in range(2,101):
    for j in range(1,100):
        b = min(i,j)
        for k in reversed(range(1,b+1)):
            ans[i][j] += ans[i-k][k]
        if j>=i:
            ans[i][j] += 1 ##3=3这种由于是被后续的数调用的，所以在这里也算一个方案
            
            
###http://mathworld.wolfram.com/PartitionFunctionP.html 还可以用欧拉的生成函数
        
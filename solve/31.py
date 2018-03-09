# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-31
"""

"""
动态规划
"""

coin = [1,2,5,10,20,50,100,200]
method = [0]*201
method[0]=1

###注意这里实际上递推了最大面值
for i in range(8):
    for j in range(1,201):
        if j-coin[i]>=0:
            method[j] += method[j-coin[i]]
print(method[200])

    
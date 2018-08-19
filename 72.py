# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:58:45 2018
pe-72
@author: strA
"""

#实际上就是求2到100w的欧拉函数的和
#https://blog.csdn.net/wu_tongtong/article/details/78953202
#欧拉函数线性筛
#https://blog.csdn.net/Lytning/article/details/24432651


#---------线性筛算出euler func前1000000
max_n = 1000001
p = []
flag = [True]*max_n
phi = [0]*max_n
for i in range(2,max_n):
    if flag[i]:
        phi[i] = i-1
        p.append(i)
    for j in p:
        if j*i>max_n-1:
            break
        flag[j*i] = False
        if i%j==0:
            phi[j*i] = j*phi[i]
        else:
            phi[j*i] = (j-1)*phi[i]

phi[1] = 1                
sum = 0
for i in range(2,max_n):
    sum += phi[i]
print(sum)
            
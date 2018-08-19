# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:45:33 2018

@author: strA
"""
import pickle
data = open('data_78.pkl','rb')
P = pickle.load(data)
i = pickle.load(data)
data.close()
del P[i]
i -= 1
def get_P(n):
    if n<0:
        return 0
    else:
        return P[n]

while P[i] != 0:
    i += 1
    if i%200==0:
        print(i)
    P.append(0)
    sign = 1
    for k in range(1,i+1):
        P[i] += sign*(get_P(i-int((1/2)*k*(3*k-1)))+get_P(i-int((1/2)*k*(3*k+1))))
        sign *= -1
    P[i] = P[i]%1000000
    if i==51936:
        print(P[i])
print(i)
        

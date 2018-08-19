# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:15:21 2018

@author: strA98
"""

"""
2*m(m+n)
"""
L_max = 1500000
L = [0]*(L_max+1)
LL = [0]*(L_max+1)

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

for m in range(2,int((L_max/2)**(1/2))+1):
    n = 1
    while n<=m:
        if (m*n)%2==0 and gcd(m,n)==1:
            S = 2*m*(m+n)
            if S>L_max+1:
                n+=1
                continue
            L[S] += 1
        n += 1

for i in range(1,L_max+1):
    for k in range(1,int(L_max/i)+1):
        LL[i*k] += L[i]

t = 0
for i in LL:
    if i==1:
        t+=1
print(t)
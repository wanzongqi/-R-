# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:21:29 2018

@author: strA
"""

##修改一下76即可

def gen_p(n):
    prime_b = [True]*(n+1)
    prime_b[1] = False
    for i in range(2,n+1):
        if prime_b[i]:
            for k in range(2,int(n/i)+1):
                prime_b[k*i] = False
    prime = []
    for i in range(2,n+1):
        if prime_b[i]:
            prime.append(i)
    return prime

n_max = 200
prime = gen_p(n_max)
m = len(prime)
ans = [[0 for j in range(m)] for i in range(250)]
ans[0] = [1 for j in range(m)]
flag = False
for i in range(2,250):
    if flag:
        break
    for j in range(m):
        for k in range(j+1):
            if prime[k]>i:
                break
            ans[i][j] += ans[i-prime[k]][k]
        if ans[i][j]>5000:
            print(i)
            flag = True
            break
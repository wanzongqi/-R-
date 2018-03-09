# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-27
"""

def func(a,b,n):
    return n**2+a*n+b

def gen_prime(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(1,n+1):
        if prime[i]:
            m = i*2
            while m<n:
                prime[m] = False
                m = m+i
    return prime

prime = gen_prime(100000)
global_max = 0
global_maxproduct = 0

def find(n):
    remain = set(range(-1000,1001))
    t = 0
    while len(remain)>0:
        discard = []
        for i in remain:
            if not(prime[func(n,i,t)]):
                discard.append(i)
        remain = remain-set(discard)
        t += 1
    return t,n*i
            

for i in range(-999,1000):
    max,max_product = find(i)
    if max>global_max:
        global_max = max
        global_maxproduct = max_product
print(global_maxproduct)
                
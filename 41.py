# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-41
"""

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

def check(n):
    n_str = str(n)
    for i in n_str:
        if int(i)>len(n_str) or int(i)==0 or n_str.count(i)>1:
            return False
    return True

primes = gen_prime(9999999)
for i in reversed(range(9999999)):
    if primes[i]:
        if check(i):
            print(i)
            break


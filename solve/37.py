# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-37
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

def gen_trunc(n):
    trunc = []
    n_str = str(n)
    for i in range(len(n_str)):
        trunc.append(int(n_str[i:]))
        trunc.append(int(n_str[:i+1]))
    return trunc

primes = gen_prime(1000000)
t = 0
n = 10
sum = 0
while t<11:
    flag = True
    for i in gen_trunc(n):
        if not(primes[i]):
            flag = False
            break
    if flag:
        t += 1
        sum += n
        print(n)
    n += 1
print(sum)

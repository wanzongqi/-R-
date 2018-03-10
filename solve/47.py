# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-47
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

prime = []
prime_1 = gen_prime(150000)
for n,p in enumerate(prime_1):
    if p:
        prime.append(n)

del prime_1

def decompose(n):
    fac = []
    while n>1:
        i = 0
        m = 1
        while prime[i]<=n:
            if n%prime[i] == 0:
                m *= prime[i]
                fac.append(prime[i])
            i += 1
        n = n//m
    return fac

n = 50000
a = [0]*150000
for i in range(500,150000):
    a[i] = len(set(decompose(i)))
    print(i)

print('done1')
while True:
    if a[n]==4 and a[n+1]==4 and a[n+2]==4 and a[n+3]==4:
        print(n)
        break
    n += 1
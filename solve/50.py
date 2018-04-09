# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-50
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
prime_1 = gen_prime(1000000)
for n,p in enumerate(prime_1):
    if p:
        prime.append(n)

max_c = 20
max_p = 0

for i in range(len(prime)):
    j = 1
    sum = prime[i]
    while sum<1000000:
       if prime_1[sum] and j>max_c:
           max_c = j
           max_p = sum
           print(max_c,max_p)
       sum += prime[i+j]
       j += 1
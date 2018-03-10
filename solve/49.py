# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-49
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
prime_1 = gen_prime(20000)
for n,p in enumerate(prime_1):
    if p and n>1000 and n<10000:
        prime.append(n)

for i in range(len(prime)):
    if prime_1[prime[i]+3330] and prime_1[prime[i]+6660] and prime[i]+6660<10000:
        if set([s for s in str(prime[i])])&set([s for s in str(prime[i]+3330)])&set([s for s in str(prime[i]+6660)])==set([s for s in str(prime[i])]):
            print(prime[i],prime[i]+3330,prime[i]+6660)
        

    
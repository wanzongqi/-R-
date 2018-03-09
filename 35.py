# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-35
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

def circle(n):
    n_str = str(n)
    number = []
    for i in range(len(n_str)):
        number.append(int(n_str[i:]+n_str[:i]))
    return number

primes = gen_prime(1000000)
count = 0
for i in range(2,1000000):
    if primes[i]:
        flag = True
        number = circle(i)
        for num in number:
            if not(primes[num]):
                flag=False
        if flag:
            count += 1
print(count)
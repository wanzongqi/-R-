# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 11:09:39 2018

@author: https://www.douban.com/note/208148392/

ProjectEuler-problem-46
"""

from math import sqrt

def is_prime(n):
    if n <= 1: 
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = 33
while True:
    if not is_prime(n):
        flag = False
        for i in range(1, int(sqrt(n/2))+1):
            a = 2 * i * i
            b = n - a
            if is_prime(b): 
                flag = True
        if not flag: 
            print(n)
            break
    n += 2 
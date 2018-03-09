# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-4
"""

def gen_palindrome(n):
    """
    从一个三位数生成一个6位的回文数
    """
    n_str = str(n)
    n_str = n_str + n_str[::-1]
    return int(n_str)

def decompose(n):
    """
    检查n是否可以分解成两个三位数乘积
    """
    for i in range(int(n/1000+1),1000):
        if n%i==0:
            return True
    return False

for i in reversed(range(100,1000)):
    n = gen_palindrome(i)
    if decompose(n):
        print(n)
        break
    
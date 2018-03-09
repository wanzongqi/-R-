# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-36
"""

def check(str):
    i = len(str)-1
    j = 0
    while i>=j:
        if str[i] != str[j]:
            return False
        i -= 1
        j += 1
    return True

def gen_palindrome(n):
    """
    生成两个回文数
    """
    n_str = str(n)
    n_str1 = n_str + n_str[::-1]
    n_str2 = n_str[:-1] + n_str[-1] + n_str[:-1][::-1]
    return int(n_str1),int(n_str2)

sum = 0
for i in range(1,1000):
    a,b = gen_palindrome(i)
    if check(bin(a)[2:]):
        sum += a
    if check(bin(b)[2:]):
        sum += b
print(sum)


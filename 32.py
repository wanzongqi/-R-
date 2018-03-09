# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-32
"""


def p32():
    min, max, sum = 1000, 10000, 0
    counted = [False]*max

    for i in range(1, min):
        for j in range(min//i, max//i):
            dig = [0]*10
            a, b, c = i, j, i*j

            while a:
                dig[a%10] += 1
                a //= 10
            while b:
                dig[b%10] += 1
                b //= 10
            while c:
                dig[c%10] += 1
                c //= 10

            pandigital = dig[0] == 0
            for digit in dig[1:]:
                if digit != 1:
                    pandigital = False
            if pandigital:
                if not counted[i*j]:
                    sum += i*j
                    counted[i*j] = True

    return sum

print(p32())
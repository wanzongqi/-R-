# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-39
"""

def gen_2():
    square = [0]*160001
    for i in range(1,401):
        square[i**2] = i
    return square

square = gen_2()
count = [0]*1000
for i in range(3,500):
    for j in range(i,999-i):
        k = i*i+j*j
        if k<160000 and square[k]>0:
            if square[k]+i+j==840:
                print(i,j,square[k])
            count[square[k]+i+j] += 1

max_n = 0
max_m = 0
for i in range(1000):
    if count[i]>max_n:
        max_n = count[i]
        max_m = i
print(max_m)        
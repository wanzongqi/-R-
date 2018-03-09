# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-23
"""
import math

#sod 来自21.py
def sod(n):
    sum = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sum = sum+i+int(n/i)
    if math.sqrt(n)-int(math.sqrt(n))<0.001:
        sum = sum-int(math.sqrt(n))
    return sum

def gen_abundant_number():
    abundant_numbers = []
    for i in range(1,28123):
        if sod(i)>i:
            abundant_numbers.append(i)
    return abundant_numbers

cannot_addition = [True]*58000
abundant_numbers = gen_abundant_number()

for i in range(len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        cannot_addition[abundant_numbers[i]+abundant_numbers[j]] = False

sum = 0
for i in range(1,28124):
    if cannot_addition[i]:
        sum += i
print(sum)
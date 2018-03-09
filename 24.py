# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-24
"""

"""
不需要枚举出来
"""
import math
digits = [0,1,2,3,4,5,6,7,8,9]
number = 1000000
total = 3628800
num = 0
for i in reversed(range(1,11)):
    dig = math.ceil((number/total)*len(digits)-1)
    num = num + digits[dig]*(10**(i-1))
    total = round(total/i)
    number = number - dig*total
    del digits[dig]
print(num)
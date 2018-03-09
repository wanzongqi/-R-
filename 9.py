# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-9
"""

"""
a=m，b=(m^2 / k - k) / 2，c=(m^2 / k + k) / 2
由勾股数的公式，问题被大大简化
"""

import math

for k in range(1,100):
    if math.sqrt(k**2+4000*k) - int(math.sqrt(k**2+4000*k))<0.01:
        kk = k
        break
    
m = (-k+math.sqrt(k**2+4000*k))/2
print(m*(((m**2)/k-k)/2)*(((m**2)/k+k)/2))
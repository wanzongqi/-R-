# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-26
"""

"""
将数去除掉所有因子2与5，得到的数是决定循环节长度的数，只需要看得到的数模10的多少次方为1
"""

def eliminate_2_5(n):
    while n%2==0:
        n = n//2
    while n%5==0:
        n = n//5
    return n


eliminated_n = [eliminate_2_5(i) for i in range(1,1000)]
#eliminated_n[n-1]代表削除2，5的n

temp_mod = [1]*1000
last = 1001
remain = set(range(1,1000))
for i,ii in enumerate(eliminated_n):
    if ii == 1:
        remain.discard(i+1)

while len(remain)>0:
    d = []
    for j in remain:
        temp_mod[j-1] = (temp_mod[j-1]*10)%eliminated_n[j-1]
        if temp_mod[j-1] == 1:
            last = j
            d.append(j)
    remain = remain - set(d)
print(last)



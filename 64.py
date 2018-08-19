# -*- coding: utf-8 -*-
"""
strA
pe-64
"""
#参考资料
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm

def cal_next(S,m,d,a):
    period = False
    m = d*a[-1]-m
    d = (S-m**2)//d
    a.append(int((a[0]+m)/d))
    if a[-1]==2*a[0]:
        period = True
    return period,m,d,a

num = 0
for S in range(2,10001):
    if int(S**(1/2))==S**(1/2):
        continue
    m = 0
    a = [int(S**(1/2))]
    d = 1
    period = False
    while not(period):
        period,m,d,a = cal_next(S,m,d,a)
    if (len(a)-1)%2==1:
        num += 1
print(num)
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:46:34 2018

@author: strA

ProjectEuler-problem-67
"""

tower = [[0 for i in range(100)] for i in range(100)]
max_path = [[0 for i in range(100)] for i in range(100)]
f = open(r'f:/content/ProjectEuler/data/67.txt','r')
for i in range(100):
    data = f.readline().split(' ')
    for j in range(i+1):
        tower[i][j] = int(data[j])

for i in range(100):
    max_path[99][i] = tower[99][i]
for i in reversed(range(99)):
    for j in range(i+1):
        max_path[i][j] = tower[i][j] + max(max_path[i+1][j],max_path[i+1][j+1])
print(max_path[0][0])
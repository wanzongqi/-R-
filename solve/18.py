# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-18
"""

"""
这一题有明显的子问题性质，可以使用动态规划求解，
"""

tower = [[0 for i in range(15)] for i in range(15)]
max_path = [[0 for i in range(15)] for i in range(15)]
f = open(r'f:/content/ProjectEuler/data/18.txt','r')
for i in range(15):
    data = f.readline().split(' ')
    for j in range(i+1):
        tower[i][j] = int(data[j])

for i in range(15):
    max_path[14][i] = tower[14][i]
for i in reversed(range(14)):
    for j in range(i+1):
        max_path[i][j] = tower[i][j] + max(max_path[i+1][j],max_path[i+1][j+1])
print(max_path[0][0])
# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-11
"""

#得到一个矩阵
def save_data():
    #array = [1]*23
    #matrix = [array]*23
    #应该如下方式定义矩阵，像上面的方式定义的矩阵会在修改时同时修改每一行
    matrix = [[0 for i in range(-3,23)] for i in range(-3,23)]
    f = open(r'f://content/ProjectEuler/data/11.txt','r')
    for i in range(20):
        str = f.readline().replace('\n','')
        num = str.split(' ')
        for j in range(20):
            matrix[i][j] = int(num[j])
    return matrix

matrix = save_data()

def max_3_direction(i,j):
    direction = [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,1),(2,2),(3,3)],[(0,0),(1,0),(2,0),(3,0)],[[0,0],[-1,1],[-2,2],[-3,3]]]
    max = 0
    
    for direc in direction:
        num = matrix[i+direc[0][0]][j+direc[0][1]]*matrix[i+direc[1][0]][j+direc[1][1]]*matrix[i+direc[2][0]][j+direc[2][1]]*matrix[i+direc[3][0]][j+direc[3][1]]
        if num>max:
            max = num
    return max

max = 0
for i in range(20):
    for j in range(20):
        num = max_3_direction(i,j)
        if num>max:
            max = num
            print(i,j)
print(max)
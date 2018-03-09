# -*- coding: utf-8 -*-
"""
@author: strA

ProjectEuler-problem-43
"""
"""
深度搜素
"""

class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []
 
    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

digits = set(['0','1','2','3','4','5','6','7','8','9'])
divide = [1,2,3,5,7,11,13]
num = []
s = Stack()
for i in range(100,999):
    if i%17==0:
        flag = True
        for st in str(i):
            if str(i).count(st)>1:
                flag = False
        if flag:
            s.push(str(i))
while s.size()>0:
    a = s.pop()
    if len(a)==10:
        num.append(int(a))
        continue
    for b in digits-set([i for i in a]):
            if int(b+a[0:2])%divide[2-len(a)]==0:
                s.push(b+a)
print(num)
print(sum(num))
    


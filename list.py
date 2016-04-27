#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
这里文件是练习python的list的练习
'''
l = ['python','java','php','javascript']

# 输出这个list的长度
print("len:%s" % len(l))

# 要删除list结尾的数据，用pop()方法
l.pop()
print('删除后：',l)

'''
练习
请用索引取出下面list的指定元素：
'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

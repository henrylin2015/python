#!/usr/bin/enb python3
# _*_ coding:utf-8 _*_
'''
python for循环
'''

'''
Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['Michael', 'Bob', 'Tracy']
'''
name = ['Michael' , 'Bob' , 'Tracy']
for item in name:
    print(item)

'''
再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
'''
sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum += i

print(sum)

'''
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
'''
print("range(5):")
for i in range(5):
    print(i)

'''
range(101)就可以生成0-100的整数序列，计算如下：
'''
sum = 0
for i in range(101):
    sum = sum + i

print('range(101)的和为：%s' % sum)

'''
练习

请利用循环依次对list中的每个名字打印出Hello, xxx!：

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
'''
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,%s!' % name)

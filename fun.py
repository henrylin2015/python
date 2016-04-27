#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

r'''
learning.py

A Python 3 tutorial from http://www.liaoxuefeng.com

Usage:

python3 learning.py
'''
import sys

def check_version():
    v = sys.version_info
    if v.major == 3 and v.minor >= 4 :
        return True
    print('Your current python is %d.%d.Please use Python 3.4' % (v.major,v.minor))
    return False

if not check_version():
    exit(1)


r'''
用户从键盘输入数据，然后输出到控制台
'''
'''
def get_name():
    return input('Please enter your name:')

print(get_name())
'''


'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
'''
def get_core():
    s1 = 72
    s2 = 85
    r = (s2-s1)/s1*100
    return ('%.2f' % r)

print("小明的成绩的百分点:%s" % get_core())
'''
'''
我们先写一个计算x2的函数：
'''

#def power(x):
#    return x * x


'''
现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
'''
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

print('power(5,5):%s' % power(5,5))

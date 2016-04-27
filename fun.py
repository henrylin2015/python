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
def get_name():
    return input('Please enter your name:')

print(get_name())

'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
def get_core():
    s1 = 72
    s2 = 85
    r = (s2-s1)/s1*100
    return ('%.2f' % r)

print("小明的成绩的百分点:%s" % get_core())

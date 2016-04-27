#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
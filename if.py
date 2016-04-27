#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
python if语句的练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

1.低于18.5：过轻
2.18.5-25：正常
3.25-28：过重
4.28-32：肥胖
5.高于32：严重肥胖
'''
m_height = 1.75
m_weight = 80.5

bmi = m_weight / (m_height * m_height)

if bmi < 18.5:
    print('过轻 bmi:%d' % bmi)
elif bmi >= 18.5 or bmi < 25:
    print('正常 bmi:%d' % bmi)
elif bmi >= 25 or bmi < 28:
    print('过重 bmi:%d' % bmi)
elif bmi >= 28 or bmi < 32:
    print('肥胖 bmi:%d' % bmi)
elif bmi >= 32:
    print('严重肥胖 bmi:%d' % bmi)
else:
    print('不符合要求 bmi:%d' % bmi)
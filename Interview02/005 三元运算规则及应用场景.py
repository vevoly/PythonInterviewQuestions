# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/22 0022 下午 11:48'

"""
为真时的结果 if 判断条件 else 为假时的结果
举个例子 ： 肥婆纳妾 数列
"""


def fn(n):
    return n if n < 2 else fn(n - 1) + fn(n - 2)




# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 11:29'

"""
python中函数参数是引用传递。
对于不可变类型（数值、字符串、元组），因变量不能修改
所以运算不会影响到变量自身；
对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量
"""


def selfAdd(a):
    a += a

a_int = 1
print(a_int)
selfAdd(a_int)
print(a_int)
a_list = [1, 2]
print(a_list)
selfAdd(a_list)
print(a_list)


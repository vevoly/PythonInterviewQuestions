# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 4:45'

"""
[i for i in range(3)]
生成器是特殊的迭代器：
1 列表表达式的[]改成()即可变成生成器
2 函数在返回值的时候出现yield就变成生成器，而不是函数
"""

a = (i for i in range(3))
print(type(a))
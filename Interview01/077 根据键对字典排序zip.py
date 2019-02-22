# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:20'

dic = {'name': 'zs', 'sex': 'man', 'city': 'bj'}

"""
根据键对字典排序，使用zip
"""

foo = zip(dic.keys(), dic.values())
print(type(foo))
foo = sorted(foo, key=lambda x: x[0])
print(type(foo))
foo = dict(foo)
print(type(foo))
print(foo)

"""
1 使用zip构造出zip对象
2 sorted对zip对象按键排序
3 直接将list转成dict
"""

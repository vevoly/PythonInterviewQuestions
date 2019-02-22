# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/23 0023 上午 12:24'

v = dict.fromkeys(['k1', 'k2'], [])
print(v)
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)

"""
{'k1': [], 'k2': []}
{'k1': 666, 'k2': [666]}
{'k1': 777, 'k2': [666]}
"""

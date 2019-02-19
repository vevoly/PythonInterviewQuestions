# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:57'

"""
re.compile是将正则表达式编译成生成一个正则表达式pattern对象，加快速度，并重复使用
"""
import re

s = '电话号码：13526650808, 哦哦'
pattern = re.compile('1[358]\d{9}')
ret = re.match(pattern, s)
# match是从开头匹配，所有匹配不到，返回None
print(ret)
ret = re.search(pattern, s)
print(ret.group(0))
ret = re.sub(pattern, '14788888705', s)
print(ret)


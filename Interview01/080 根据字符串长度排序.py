# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 7:43'

s = ['ab', 'abc', 'd', 'efdfs', 'sdss']
print(s)
a = sorted(s, key=lambda x: len(x))
print(a)
s.sort(key=len)
print(s)


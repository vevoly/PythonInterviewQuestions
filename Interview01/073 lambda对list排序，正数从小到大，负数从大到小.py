# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 4:57'

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]

a = sorted(foo, key=lambda x: (x < 0, abs(x)))

print(a)


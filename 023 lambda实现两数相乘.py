# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 10:59'

fn = lambda a, b: a * b
print(fn(10, 12))

fn = lambda a, b: abs(a) * b if a < 0 else a * b
print(fn(-10, 12))
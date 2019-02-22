# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 7:59'

a = 5
b = 6

def fn():
    global a
    a = 3
    b = 3


fn()

print(a, b)

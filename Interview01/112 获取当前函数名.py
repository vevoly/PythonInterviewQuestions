# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/19 0019 下午 7:17'

import inspect


def who_am_i():
    return who_am_i.__name__

print(who_am_i())


def who_am_i2():
    return getattr(who_am_i2, '__name__')

print(who_am_i2())
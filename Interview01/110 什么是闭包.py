# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/19 0019 下午 5:53'
"""
如果一个内部函数有对外部作用于的引用，那么这个内部函数就是一个闭包。
在使用时，可以直接调用内部函数，内部函数也照样可以使用外部函数的变量。
"""


def outter():
    a = 1 # a为内部作用域

    def inner():
        print(a)

    return inner

outter()

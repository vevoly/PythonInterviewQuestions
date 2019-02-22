# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/19 0019 下午 5:53'
"""
装饰器就是在给原有函数加装饰。
在不修改原有函数的基础上添加新的功能。
比如：
原有功能函数method1、method2，要给原有功能函数添加计算函数执行时间的功能，
并且不能修改原有函数，因为原有函数可能已经在很多地方使用，轻易修改会造型系统崩溃。
"""

import time


def method1():
    time.sleep(2)
    print('method1')


def method2():
    time.sleep(3)
    print('method2')

"""
给两个函数添加计算执行时间功能
"""


def perform_time1(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(end_time - start_time)

perform_time1(method1)
perform_time1(method2)

print('-------------------')
"""
可以使用闭包的方法，使程序更简单
"""


def perform_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return inner

method1 = perform_time(method1)
method1()
# 使用装饰器的方法调用

@perform_time
def method3():
    time.sleep(0.3)
    print('method3')

method3()

# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 8:56'

"""
fun(*args、**kwargs)中的*args, **kwargs什么意思？
*args和**kwargs主要用于函数定义，将不定量的参数传递给一个函数。
*args传送一个非键值对的可变数量的参数
**kwargs传递一个键值对的可变数量参数
例如：
"""


def demo(*args):
    for x in args:
        print(x)


demo(0, 3, 1, 3)
print('---------------------------')


def demo1(arg, *args):
    print(arg)
    for x in args:
        print(x)


demo1('a', 'b', 'c', 'd', 'e')
print('---------------------------')


def demo2(**kwargs):
    for k, v in kwargs.items():
        print('{0} = {1}'.format(k, v))


demo2(name='python', age=10)
print('---------------------------')






# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 10:45'

"""
不可变数据类型：数值型、字符串、元组tuple
不允许变量的值发生变化，如果改变变量的值，相当于新建了对象，
而对于相同值的对象，在内存中则只有一个地址
"""

a = 3
b = 3
print(id(a))
print(id(b))
b = 4
print(id(b))

"""
可变数据类型：list、dict
允许变量的值发生变化，即如果对变量进行append、+=等这类操作，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
不过对于相同的值的不同对象，在内存中则会存在不同的地址，
相当于内存中对于同值的对象保存了多份，这里不存在引用计数。
"""
a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))



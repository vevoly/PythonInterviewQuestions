# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:16'

foo = [
    ['zs', 19],
    ['ll', 54],
    ['wa', 23],
    ['df', 23],
    ['xf', 23]
]
a = sorted(foo, key=lambda x: x[0])
print(a)

a = sorted(foo, key=lambda x: x[1])
print(a)

# 如果年龄相等，就根据姓名排序
a = sorted(foo, key=lambda x: (x[1], x[0]))
print(a)
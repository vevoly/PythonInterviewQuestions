# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:12'

foo = [
    ('zs', 19),
    ('ll', 54),
    ('wa', 17),
    ('df', 23)
]

a = sorted(foo, key=lambda x: x[0], reverse=True)
print(a)
a = sorted(foo, key=lambda x: x[1])
print(a)

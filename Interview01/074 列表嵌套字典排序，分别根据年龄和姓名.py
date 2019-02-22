# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:08'

foo = [
    {'name': 'zs', 'age': 19},
    {'name': '||', 'age': 54},
    {'name': 'wa', 'age': 17},
    {'name': 'df', 'age': 23}
]

a = sorted(foo, key=lambda x: x['age'], reverse=True)
print(a)
a = sorted(foo, key=lambda x: x['name'])
print(a)

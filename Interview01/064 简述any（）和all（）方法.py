# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 3:53'

"""
any()：只要迭代器中有一个元素为真就为真
all()：迭代器中所有的判断返回都为真，结果才为真

python中什么元素为假?
0, 空字符串，空列表，空字典，空元组，None， False
"""

a = [True, False]
print(any(a))   # True
print(all(a))   # False

print('------------')
a = ''
print(any(a))   # False
print(all(a))   # True


print('------------')
b = ['good', 'bad', 'excellent', '']
print(any(b))   # True
print(all(b))   # False


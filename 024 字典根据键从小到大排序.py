# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:02'
"""
字典按键从小到大排序
"""
d = {
    'name': 'python',
    'age': '20',
    'city': '广州',
    'tel': '13526650805',
    'hobby': 'play'
     }

d1 = dict(sorted(d.items()))
print(d1)
print('---------------------------------------')
# 上面的等于下面的
# d1 = sorted(d.items(), key=lambda i: i[0], reverse=False)
# d1 = dict(d1)

"""
第二种方法
l1 = sorted(d.items())
print(l1)
d1 = dict((k, v) for k, v in tuple(l1))
print(d1)
print('----------------------------')
"""

# 按值从大到小排序
d2 = dict(sorted(d.items(), key=lambda a: a[1], reverse=True))
print(d2)

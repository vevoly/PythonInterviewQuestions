# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:02'

d = {
    'name': 'python',
    'age': '20',
    'city': '广州',
    'tel': '13526650805',
    'hobby': 'play'
     }

l1 = sorted(d.items())
# 上面的等于下面的
# l1 = sorted(d.items(), key=lambda i: i[0], reverse=False)
print(l1)
d1 = dict((k, v) for k, v in tuple(l1))
print(d1)

print('----------------------------')
# 按值从大到小排序
l2 = sorted(d.items(), key=lambda a: a[1], reverse=True)
print(l2)
print(dict((k, v) for k, v in tuple(l2)))

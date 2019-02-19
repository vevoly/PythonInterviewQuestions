# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 8:04'

d = dict()
d['name'] = 'python'
d['age'] = 20
print(d)
# 删除键name
del d['name']
print(d)
d.pop('age')
print(d)

# d2
d2 = {'name': 'java'}
# d合并d2
d.update(d2)
print(d)

seq = ('name', 'age', 'sex')
print({}.fromkeys(seq))
print({}.fromkeys('abc'))
print({}.fromkeys(['a', 'b', 'c'], 10))
print({}.fromkeys(('a', 'b', 'c'), 10))
print({}.fromkeys((('a', 1), ('b', 2), ('c', 3))))
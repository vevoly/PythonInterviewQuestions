# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:39'

a = zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))
a0 = dict(a)
a1 = range(10)
a2 = [i for i in a1 if i in a0]
a3 = [a0[s] for s in a0]
"""
说明：
a0是字典
for s in a0
s的结果为字典a0的键
a0[s]当然就是字典a0的值
"""

print('a0', a0)
print(list(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))))
print('a2', a2)
print('a3', a3)

"""
结果:
a0: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
[]
[1, 2, 3, 4, 5]
"""

"""
如果a2 = [i for i in a1 if i in a0.values()]
结果就是[1, 2, 3, 4, 5]
如果a2 = [i for i in a1 if i not in a0.values()]
结果是[0, 6, 7, 8, 9]

"""
print('-------------------------')
a2 = [i for i in a1 if i in a0.values()]
print(a2)
a2 = [i for i in a1 if i not in a0.values()]
print(a2)

for s in a0:
    print(s)
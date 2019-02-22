# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:29'

dic = {'name': 'zs', 'sex': 'man', 'city': 'bj'}

foo = dic(sorted(dic.items(), key=lambda x: x[0]))
print(foo)

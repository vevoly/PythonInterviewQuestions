# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:55'

a = list(range(1, 11))
ret = [i for i in a if i %2 ==1]
print(ret)

ret = [i for i in a if i %2 ==0]
print(ret)
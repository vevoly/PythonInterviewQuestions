# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 6:33'
import random


l = [i for i in range(10)]
print(l)
t = (i for i in range(10))
print(t)
dic = {k: random.randint(4, 9) for k in ['a', 'b', 'c', 'd', 'e']}
print(dic)

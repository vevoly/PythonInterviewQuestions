# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:01'


def sum(n):
    if n < 1:
        return 0
    else:
        return n + sum(n-1)


ret = sum(10)
print(ret)




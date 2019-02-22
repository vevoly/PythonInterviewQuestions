# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:01'


def summ(n):
    if n:
        return n + summ(n - 1)
    else:
        return 0

print(summ(100))






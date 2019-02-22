# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 12:53'

try:
    for i in range(5):
        if i > 2:
            raise Exception('数字大于2')
except Exception as e:
    print(e)


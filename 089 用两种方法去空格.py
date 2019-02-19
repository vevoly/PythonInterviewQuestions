# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:28'

# 第一种方法
str = 'hello world ha ha'
ret = str.replace(' ', '')
print(ret)

# 第二种方法
l = str.split(' ')
print(l)
ret = ''.join(l)
print(ret)

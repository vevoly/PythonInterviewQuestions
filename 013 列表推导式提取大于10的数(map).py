# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 9:34'

"""
列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25],并
使用列表推导式取出大于10的数，最终输出[16,25]
"""
l = [1, 2, 3, 4, 5]


def fn(x):
    return x**2


l1 = map(lambda x: x*x, l)
# print(type(l1))
l1 = [i for i in l1 if i > 10]
print(l1)


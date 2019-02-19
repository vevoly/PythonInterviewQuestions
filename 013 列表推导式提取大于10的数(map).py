# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 9:34'

"""
1 列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25],并
2 使用列表推导式取出大于10的数，最终输出[16,25]
"""
l = [1, 2, 3, 4, 5]

# map用来替代循环
l = list(map(lambda x: x*x, l))
print(l)
print('----------------------------')

# 列表推导式
l1 = [i for i in l if i > 10]
print(l1)
print('----------------------------')

# filter
l2 = list(filter(lambda x: x > 10, l))
print(l2)






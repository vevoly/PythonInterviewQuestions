# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:35'

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，
返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，
序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表
"""
a = list(range(1, 11))
print(a)
ret = list(filter(lambda x: x % 2 == 1, a))
print(ret)












# f = filter(lambda a: a %2 == 1, a)
# # print(type(f))
# ret = [i for i in f]
# print(ret)
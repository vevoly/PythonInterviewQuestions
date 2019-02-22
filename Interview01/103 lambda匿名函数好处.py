# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 11:39'

"""
精简代码，lambda省去了定义函数，map省去了写for循环的过程
"""

a = ['苏州', '中国', '哈哈', '', '', '日本', '', '', '德国']
ret = list(map(lambda x: '填充物' if x == '' else x, a))
print(ret)

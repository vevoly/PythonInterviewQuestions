# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 12:56'

"""
(.*)贪婪匹配，会把满足正则的尽可能多的往后匹配
(.*?)非贪婪匹配，会把满足正则的尽可能少的匹配
"""
import re

s = '<a>哈哈</a><a>呵呵</a>'
ret1 = re.findall('<a>(.*)</a>', s)
print(ret1)
ret2 = re.findall('<a>(.*?)</a>', s)
print(ret2)

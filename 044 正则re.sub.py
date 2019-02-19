# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 11:33'
"""
a="张明 98分"，用re.sub，将98替换为100
"""
import re
a = "张明 98分"
p = '\d+'
pattern = re.compile(p)
ret = re.sub(pattern, '100', a)
print(ret)
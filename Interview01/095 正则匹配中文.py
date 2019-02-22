# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 9:18'
import re

title = '你好，hello， 世界'

p = '[\u4e00-\u9fa5]+'
ret = re.findall(p, title)
print(ret)

# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 7:51'

"""
s="info:xiaoZhang 33 shandong"
用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
"""
import re
s = "info:xiaoZhang 33 shandong"
p = ':| '
# pattern = re.compile(p)
ret = re.split(p, s)
print(ret)

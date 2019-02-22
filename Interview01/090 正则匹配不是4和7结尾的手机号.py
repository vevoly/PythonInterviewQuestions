# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:31'

import re

tels = ['13100000004', '13526650808', '14788888705', '13669787807']

p = '^1[3|4|8]\d{8}[4|7]$'
for tel in tels:
    ret = re.match(p, tel)
    if ret:
        print('匹配成功', ret.group())
    else:
        print('匹配失败', tel)



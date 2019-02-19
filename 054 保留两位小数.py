# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:00'

"""
a = "%.03f"%1.3335
计算a的结果1.333
'%.Nf'%??? 表示保留N位小数
"""
a = "%.02f" % 1.3335
print(a)

b = round(float(a), 2)
print(b)

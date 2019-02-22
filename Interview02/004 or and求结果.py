# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/22 0022 下午 11:24'

v1 = 1 or 3
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
v6 = 0 or False and 1
v7 = 0 or 0
v8 = False or False
"""
对于and操作符：
只要左边的表达式为真，整个表达式返回的值是右边表达式的值，否则，返回左边表达式的值
左真则右，左假则左

对于or操作符：
只要两边的表达式为真，整个表达式的结果是左边表达式的值
如果是一真一假，返回真值表达式的值
如果两个都是假，比如空值和0，返回的是右边的值。（空值或0）

二真则左，二假则0，一真则真

顺口溜：
not and or
and：左真则右，左假则左
or： 二真则左，二假则0，一真则真
"""
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)
print(v8)
"""
答案
1
3
0
1
1
False
0
False
"""
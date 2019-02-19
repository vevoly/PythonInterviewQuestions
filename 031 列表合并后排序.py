# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 12:11'
"""
两个列表[1,5,7,9]和[2,2,6,8]合并为
[1,2,2,5,6,7,8,9]
"""
list1 = [1, 5, 7, 9]
list2 = [2, 2, 6, 8]
list3 = list1 + list2
list3.sort()
print(list3)
print('_--------------------_')

list1.extend(list2)
print(list1)
list1.sort()
print(list1)


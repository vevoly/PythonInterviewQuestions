# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 12:12'
"""
利用min方法求出最小值，原列表删除最小值，新列表加入最小值，
递归调用获取最小值函数
"""
list = [2, 3, 5, 4, 9, 6]
new_list = []


def list_sort(list):
    m = min(list)
    new_list.append(m)
    list.remove(m)
    if list:
        list_sort(list)
    return new_list
print(list_sort(list))








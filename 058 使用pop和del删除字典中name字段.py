# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:32'

"""
使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
"""

dic = {"name":"zs","age":18}
dic.pop('name')
print(dic)

dic = {"name":"zs","age":18}
del dic['name']
print(dic)
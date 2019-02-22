# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 1:09'

"""
x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
"""

x = "abc"
y = "def"
z = ["d","e","f"]
print(x.join(y))
print(x.join(z))

"""
join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
"""

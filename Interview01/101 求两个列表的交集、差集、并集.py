# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 11:33'

a = [1, 2, 3, 4]
b = [4, 3, 5, 6]

# 交集
jj = set(a).intersection(set(b))
print(jj)
# 并集
bj = set(a).union(set(b))
print(bj)
# 差集
cj = set(a).difference(set(b))
print(cj)

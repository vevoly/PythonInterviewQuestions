# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 8:14'

l = [11, 12, 13, 12, 36, 25, 13, 11]
print(l)
print('------------------')
# 第一种方法：set
l1 = list(set(l))
print(l1)
print('------------------')
# 第二种方法：fromkeys
l2 = list({}.fromkeys(l).keys())
# l2 = {}.fromkeys(l)
# print(l2)
# l2 = l2.keys()
# print(l2)
# l2 = list(l2)
# fromkeys用户创建一个新字典，以序列seq中元素做字典的键，value为字典所有键的初始值
print(l2)
print('------------------')
# 第三种方法：循环遍历
l3 = []
for i in l:
    if i not in l3:
        l3.append(i)
print(l3)
print('------------------')
# 第四种方法：按照索引再次排序
l4 = list(set(l))
l4.sort(key=l.index)
print(l4)
l4.sort()
print(l4)




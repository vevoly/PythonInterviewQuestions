# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 10:52'

s = 'sjdkfljaskldfjlksjdflksjdkfljs'
s1 = list(set(s))
s1.sort()
# s1.sort(reverse=True) reverse 反序排列
s1 = ''.join(s1)
print(s1)

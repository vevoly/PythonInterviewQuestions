# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/23 0023 上午 12:08'

s = 'abcdefg'
s1 = s.upper()
print(s1)
s2 = s.lower()
print(s2)
s3 = s.title()
print(s3)
s4 = s.replace('c', 'z')
print(s4)
s5 = s.count('a')
print(s5)

print('------------------------------')

l = ['a', 'b', 'c', 'd', 'e']
l.append('f')
print(l)
l2 = l.pop()
print(l2)
l3 = l.count('a')
print(l3)
l.remove('e')
print(l)
l.sort(key=lambda x: x, reverse=True)
print(l)

print('------------------------------')

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.get('a'))
print(d.pop('b'))

# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 10:00'

"""
<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
"""

import re

str = '<div class="nam">中国</div>'
pattern = '<div class=".*">(.*?)</div>'
p = re.compile(pattern)
ret = re.findall(pattern, str) # 这种方法也可以
# ret = p.findall(str)
print(ret)

# re.match 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none。
regx = re.compile(pattern)
# re.compile 用于编译正则表达式，生成一个正则表达式pattern对象，
# 供match和search两个函数使用
ret = re.match(regx, str)
print(ret.group(1))

# re.search 扫描整个字符串并返回第一个成功的匹配。
ret = re.search(pattern, str)
print(ret.group(1))

"""
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
"""

"""
将中国替换成日本
"""
pattern = '>.*<'
ret = re.sub(pattern, '>日本<', str)
print(ret)

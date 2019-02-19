# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:27'

"""
字符串a = "not 404 found 张三 99 深圳"，
每个词中间是空格，
用正则过滤掉英文和数字，最终输出"张三  深圳"
"""
import re

a = "not 404 found 张三 99 深圳"
pattern = '\d+|[a-zA-Z]+'
ret = re.sub(pattern, '', a).strip()
print(ret)
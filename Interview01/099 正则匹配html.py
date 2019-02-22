# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 10:06'

import re

labels = ['<html><h1>www.itcast.cn</h1></html>', '<html><h1>www.itcast.cn</h2></html>']

for label in labels:
    ret = re.match(r'<(\w*)><(\w*)>.*?</\2></\1>', label)
    if ret:
        print('%s 是符合要求的标签' % ret.group())
    else:
        print('%s 不符合要求' % label)

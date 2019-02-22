# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 12:17'

import datetime

t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
w = datetime.datetime.now().weekday()
print(t)
print(w)
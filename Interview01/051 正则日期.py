# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 12:05'
import re

url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

ret = re.findall('dateRange=(.*?)%7C(.*?)&', url)
print(ret)
print('--------------------------------------------')
pattern = re.compile('\d{4}-\d{2}-\d{2}')
ret = pattern.findall(url)
print(ret)
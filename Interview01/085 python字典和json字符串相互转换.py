# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:18'

import json


dic = {'name': 'zs'}
ret = json.dumps(dic)
print(ret, type(ret))
ret = json.loads(ret)
print(ret, type(ret))



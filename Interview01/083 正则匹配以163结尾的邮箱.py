# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 7:55'

import re

email_list = ['xiaowang@163.com', 'xiaozhang@163.coma', 'aa@qq.com']
p = '[\w]{4,20}@163\.com$'
for email in email_list:
    ret = re.match(p, email)
    if ret:
        print('%s 符合要求，匹配结果：%s' % (email, ret.group()))
    else:
        print('%s 不符合要求' % email)


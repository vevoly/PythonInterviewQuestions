# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 7:46'

"""
当以字符串格式化书写方式的时候，用户输入;+sql语句，后面的sql语句会执行
"""

name = 'zs'
sql = 'select * from demo where name="%s"' % name
print('正常sql语句', sql)

name = 'zs;drop database demo'
sql = 'select * from demo where name="%s"' % name
print('sql注入语句', sql)

"""
解决方法：通过传参数方式解决sql注入
"""
params = [name]
count = cs.execute('select * from goods where name=%s', params)

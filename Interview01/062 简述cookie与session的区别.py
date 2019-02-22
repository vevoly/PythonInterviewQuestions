# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 3:40'

"""
1 session运行在服务器端，cookie在客户端
2 session运行依赖session id， 而session id是存在cookie中的，也就是说
如果浏览器禁用了cookie，同时session也会失效，存储session时，建与cookie中
的sessionid相同，值是开发人员设置的键值对信息，进行了base64加密，过期时间由开发人员设置。
3 cookie安全性比session差
"""
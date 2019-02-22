# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 3:36'

"""
同源策略需要同时满足以下三点要求：
1 协议相同
2 域名相同
3 端口相同

http:www.test.com与https:www.test.com不同源，协议不同
http:www.test.com与http:www.admin.com不同源，域名不同
http:www.test.com与http:www.test.com:8080不同源，端口不同
"""



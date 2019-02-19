# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:27'

"""
前端：
1 减少http请求
2 html和css放在页面上部，js放在页面下部。
因为js加载比html和css慢，所以要优先加载html和css，
以防页面显示不全，性能差，也影响用户体验
"""

"""
后端：
1 缓存存储读写次数高，变化少的数据，比如网站首页信息、商品信息等。
应用程序读取数据时，一般先是从缓存中读取，如果读取不到货数据失效，
再访问磁盘数据库，并将数据再次放入缓存。
2 异步方式，如果有耗时的操作，可以采用异步方式，比如celery
3 代码优化，避免循环和判断次数太多，如果多个if else判断，
优先判断最有可能先发生的情况
"""

"""
数据库
1 如有条件，数据可以放入redis，读取速度快
2 建立索引、外键等
"""
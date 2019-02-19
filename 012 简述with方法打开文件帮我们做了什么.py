# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 9:28'


with open('./1.txt', 'wb') as f:
    f.write('hello')



f = open('./1.txt', 'wb')
try:
    f.write('hell')
except:
    pass
finally:
    f.close()

"""
打开文件在进行读写的时候可能会出现一些异常，如果按照
常规f.open的写法，我们需要使用try，except来捕获异常，
并且文件最终不管什么情况都要关闭。
with方法帮助我们实现了finally中的f.close
"""
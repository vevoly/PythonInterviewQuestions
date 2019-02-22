# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 1:00'

"""
orm object relation mapping 对象关系映射
实现了数据模型与数据库的解耦，通过简单的配置就可以更换数据库，
而不需要修改代码，只需面向对象编程。orm操作本质上会根据对接的数据库引擎，
翻译成对应的sql语句，所有使用django开发的项目无需关心程序底层使用的mysql、
oracle、sqlite。。。如果数据库迁移，只需更换数据库引擎即可
"""
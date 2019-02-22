# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 8:20'

"""
1 InnoDB 支持事务， MyISAM不支持事务。

2 MyISAM 查询、插入数据数据比较快，InnoDB适合频繁修改以及涉及到安全性比较高的应用

3 InnoDB 支持外键，MyISAM不支持。

4 对于自增长字段，InnoDB中必须包含只有该字段的索引，
但是在MyISAM表中可以和其它字段一起建立联合索引。

5 清空整个表的时候，InnoDB是一行一行的删除，效率非常慢。
MyISAM则会重建表

"""
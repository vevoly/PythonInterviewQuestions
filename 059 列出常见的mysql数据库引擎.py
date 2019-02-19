# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:34'

"""
InnoDB:
支持事务处理，支持外键，支持崩溃修复能力和并发控制。
如果需要对事务的完整性要求较高（比如银行），要求实现并发控制（比如售票），
那选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。

MyISAM:
插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读取
记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求低，可以使用。

MEMORY:
所有数据都在内存中，数据处理速度快，但不安全。如果需要很快的读写速度，对数据安全性
要求不高，可以使用。它对表的大小有要求，不能建立太大的表。
这类数据库只使用在相对较小的数据表。
"""
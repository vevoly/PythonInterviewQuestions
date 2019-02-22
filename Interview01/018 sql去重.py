# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 10:29'

"""
数据表student有id,name,score,city字段，
其中name中的名字可有重复，需要消除重复行,请写sql语句
"""

sql = "select distinct name, id, score, city from student"
# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/22 0022 下午 9:38'

"""
1 String 字符串
set name 'abc'
get name

2 Hash 键值对集合
每个hash可以存储2的32次方-1键值对（40多亿）
hmset myhash field1 'hello' field2 'world'
hget myhash field1

3 list 列表
lpush abc redis
lpush abc mangodb
lpush abc rabitmq
lrange abe 0 10
1) 'rabitmq'
2) 'mangodb'
3) 'redis'

4 set 集合
sadd abc redis
sadd abc mangodb
sadd abc rabitmq
sadd abc rabitmq
smembers abc
1) redis
2) rabitmq
3) mangodb

5 zset 有序集合
每个元素都会关联一个double类型的分数。
redis正是通过分数来为集合中的成员进行从小到大排序
zadd abc 0 redis
zadd abc 0 mangodb
zadd abc 0 rabitmq
zadd abc 0 rabitmq
zrangebyscore abc 0 1000
1) mangodb
2) rabitmq
3) redis
"""
# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 2:09'


def fn(k, v, dic={}):
    dic[k] = v
    print(dic)


fn('one', 1)
fn('two', 2)
fn('three', 3, {})

"""
结果：
{'one': 1}
{'one': 1, 'two': 2}
{'three': 3}
"""
"""
解释：
fn('one', 1)：直接将键值传递给字典
fn('two', 2)：因为字典在内存中是可变数据类型，
所以指向同一个地址，传了新值相当于给字典增加键值对。
fn('three', 3, {})：由于传了新的字典，所以不再是原先默认参数字典。
"""
d = dict()
d['five'] = 5
d['six'] = 6
fn('four', 4, d)


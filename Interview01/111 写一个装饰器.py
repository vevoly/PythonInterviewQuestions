# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/19 0019 下午 6:13'

import time
import datetime


def perform_time_logger(is_logger=False):
    """
    计算函数执行时间，并打印日志
    :param is_logger: 是否打印日志
    :return:
    """
    def perform_time(func):

        def inner(*args, **kwargs):
            start_time = time.time()
            ret = func(*args, **kwargs)
            end_time = time.time()
            print('%s(%s,%s)执行%s秒' % (func.__name__, args, kwargs, end_time - start_time))
            if is_logger:
                print('{0} -- 执行{1}({2}, {3}) -- 执行结果:{4}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), func.__name__, args, kwargs, str(ret)))
            return ret

        return inner
    return perform_time


@perform_time_logger(True)
def summ(*args, **kwargs):
    ret = 0
    if args:
        for arg in args:
            ret += arg
    elif kwargs:
        for arg in kwargs.values():
            ret += arg
    return ret



print(summ(1, 2, 3, 4, 5))







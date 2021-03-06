# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 9:19'

"""
__init__是初始化方法，创建对象后，立即被调用，可接收参数
1 __new__至少要有一个参数cls，代表当前类，此参数在实例化时由python解释器自动识别
2 __new__必须有返回值，返回实例化出来的实例，可以return父类（通过super（当前类名，cls））__new__出来实例，
或者直接是object的__new__出来的实例。
3 __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化动作，
__init__不需要返回值
4 如果__new__创建的是当前实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来
保证是当前实例，如果是其它类的类名，那么实际创建返回的就是其他类实例，其实就不会调用当前类的__init__函数，
也不会调用其它类的__init__函数。
"""


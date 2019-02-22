# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 1:54'


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton('liu', 20)
b = Singleton('liu', 30)
c = Singleton('wang', 23)

print(id(a))
print(id(b))
print(id(c))

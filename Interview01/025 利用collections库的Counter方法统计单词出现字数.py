# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/15 0015 下午 11:23'

from collections import Counter

str = 'ksdfjljsdklfjlskdjflksjdlfjsdfj,jsldjfls,;sdfsdk.,sdfs29ujlklnmkl,.m.,'
ret = Counter(str)
print(type(ret))
print(ret)
print(ret.get('s'))

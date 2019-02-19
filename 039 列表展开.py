# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 上午 1:03'

"""
[[1,2],[3,4],[5,6]]一行代码展开该列表，
得出[1,2,3,4,5,6]
"""
l = [[1, 2], [3, 4], [5, 6, 7]]
l1 = [j for i in l for j in i]
print(l1)


"""
import numpy as np
l2 = np.array(a).flatten().tolist()
print(l2)
"""
# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/23 0023 上午 12:29'

def num():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in num()])

"""
结果：[6, 6, 6, 6] 不知道为什么
"""

""" 
0, 1, 2, 3
0, 1, 4, 9
num = [0, 1, 4, 9]
0, 1, 4, 9

"""

# print(3(2))

"""
解释：
以上代码的输出是 [6, 6, 6, 6] （而不是 [0, 2, 4, 6]）。

这个的原因是 Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。所以结果是，当任何 multipliers() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，到那时，无论哪个返回的函数被调用，for 循环都已经完成了，i 最后的值是 3，因此，每个返回的函数 multiplies 的值都是 3。因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 （比如： 3 x 2）。

（顺便说下，正如在 The Hitchhiker’s Guide to Python 中指出的，这里有一点普遍的误解，是关于 lambda 表达式的一些东西。一个 lambda 表达式创建的函数不是特殊的，和使用一个普通的 def 创建的函数展示的表现是一样的。）

这里有两种方法解决这个问题。

最普遍的解决方案是创建一个闭包，通过使用默认参数立即绑定它的参数。例如：

def num():    
   return [lambda x, i=i : i * x for i in range(4)]
复制代码
另外一个选择是，你可以使用 functools.partial 函数：

from functools import partial
from operator import mul
def num():
   return [partial(mul, i) for i in range(4)]

"""
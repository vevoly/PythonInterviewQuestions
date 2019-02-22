# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/16 0016 下午 9:52'

"""
linux允许命令执行结果重定向到一个文件
将本应显示在中段上的内容输出/追加到指定文件中
> 表示输出，会覆盖文件原有的内容
>> 表示追加，会将内容追加到已有的文件末尾
用法实例：
将echo输出的信息保存到1.txt
echo Hello Python > 1.txt
将tree输出追加到1.txt
tree >> 1.txt
"""
# _*_ coding: utf-8 _*_
__author__ = 'jevoly'
__date__ = '2019/2/19 0019 下午 5:30'

dict1 = dict([['id', '1'], ['name', 'vevoly'], ['gender', 'male']])
dict2 = {
            'id': '2',
            'name': 'wang',
            'gender': 'female'
        }
print(dict1)
print(dict2)
print('--------------------')

key_list = ['id', 'name', 'gender']
dict3 = dict.fromkeys(key_list, 3)
print(dict3)
print('--------------------')
dict4 = {}.fromkeys(key_list, [1, 2, 3])
print(dict4)
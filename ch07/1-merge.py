# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,4,3,2,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print('=' * 20)
print (right)
#    id    Name subject_id
# 0   1    Alex       sub1
# 1   2     Amy       sub2
# 2   3   Allen       sub4
# 3   4   Alice       sub6
# 4   5  Ayoung       sub5
# ====================
#    id   Name subject_id
# 0   1  Billy       sub2
# 1   2  Brian       sub4
# 2   3   Bran       sub3
# 3   4  Bryce       sub6
# 4   5  Betty       sub5

# 在一个键上合并两个数据帧
# 默认是内连接，所以相同id的行就会被合并，合并成一行
# 如果列名相同，则会在尾部加上_x和_y
print('=' * 20)
print(pd.merge(left, right, on = 'id'))
#    id  Name_x subject_id_x Name_y subject_id_y
# 0   1    Alex         sub1  Billy         sub2
# 1   2     Amy         sub2  Brian         sub4
# 2   3   Allen         sub4   Bran         sub3
# 3   4   Alice         sub6  Bryce         sub6
# 4   5  Ayoung         sub5  Betty         sub5

# 在一个键上合并多个数据帧
# 内连接，即返回交集，所以只有'id', 'subject_id'这两列都一样的行才会被合并成一行
print('=' * 20)
print(pd.merge(left, right, on = ['id', 'subject_id']))
#    id  Name_x subject_id Name_y
# 0   4   Alice       sub6  Bryce
# 1   5  Ayoung       sub5  Betty

# how参数默认为'inner'，即内连接，可以修改参数，这里不再赘述

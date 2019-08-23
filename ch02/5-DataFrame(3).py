# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 数据帧的选择
# 结论：Pandas中，如果用字典构造系列和数据帧，如果强行指定index或者column，
# 则以强行指定的为准，指定的index或者column中没有，但是字典本身有的数据将被忽略，
# 指定的index或者column中有，但是字典本身没有的数据将被置NaN
dic = {'col1' : pd.Series(np.arange(4),index = ['one', 'two', 'three', 'four']),
       'col2' : pd.Series(np.arange(100, 100 + 4), index = ['one', 'two', 'three', 'four'])}
df = pd.DataFrame(dic)
print(df)

#        col1  col2
# one       0   100
# two       1   101
# three     2   102
# four      3   103

# 选中col1这一列
print(df['col1'])

# one      0
# two      1
# three    2
# four     3
# Name: col1, dtype: int32

# 列添加，感觉类似字典的添加
df['col3'] = pd.Series(np.arange(10, 10 + 4), index = ['one', 'two', 'three', 'four'])
print(df)

#        col1  col2  col3
# one       0   100    10
# two       1   101    11
# three     2   102    12
# four      3   103    13

# 这个操作很骚，第四列是前两列的和
df['col4'] = df['col1'] + df['col2']
print(df)

#        col1  col2  col3  col4
# one       0   100    10   100
# two       1   101    11   102
# three     2   102    12   104
# four      3   103    13   106

# 列删除
# 方法一 del
del df['col1']
print(df)

#        col2  col3  col4
# one     100    10   100
# two     101    11   102
# three   102    12   104
# four    103    13   106

# 方法二 pop
df.pop('col3')
print(df)

#        col2  col4
# one     100   100
# two     101   102
# three   102   104
# four    103   106
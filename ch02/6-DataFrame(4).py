# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 数据帧的行选择

dic = {'col1' : pd.Series(np.arange(4),index = ['one', 'two', 'three', 'four']),
       'col2' : pd.Series(np.arange(100, 100 + 4), index = ['one', 'two', 'three', 'four'])}
df = pd.DataFrame(dic)
print(df)
#        col1  col2
# one       0   100
# two       1   101
# three     2   102
# four      3   103

# 选择'one'那一行
print(df.loc['one'])
# col1      0
# col2    100
# Name: one, dtype: int32

# 选择第一行
print(df.iloc[0])
# col1      0
# col2    100
# Name: one, dtype: int32

# 行切片

# 输出前三行
print(df[:3])
#        col1  col2
# one       0   100
# two       1   101
# three     2   102

# 输出后三行，注意这里和python不一样
print(df[-3:])

#        col1  col2
# two       1   101
# three     2   102
# four      3   103

# 添加行
# append和python不一样，append有返回值，并且不改变原有数据
df2 = pd.DataFrame({'col1' : 100, 'col2' : 119}, index = ['five'])
df = df.append(df2) # 必须得接收返回值
print(df)

#        col1  col2
# one       0   100
# two       1   101
# three     2   102
# four      3   103
# five    100   119

# 数据帧允许index的内容重复
# 行的删除，需要制定index的内容，内容一样的所有行都将被删除

df3 = pd.DataFrame(np.array([[110, 120]]), index = ['one'], columns = ['col1', 'col2'])
df = df.append(df3)
print(df)

#        col1  col2
# one       0   100
# two       1   101
# three     2   102
# four      3   103
# five    100   119
# one     110   120

# 删除index为one的那若干行
# 同样，这个drop也有返回值
df = df.drop('one')
print(df)

#        col1  col2
# two       1   101
# three     2   102
# four      3   103
# five    100   119


# at[]用于获取指定index内容的元素值
print(df.at['two', 'col1']) # 1

# iat[]用于获取指定index下标的元素值
print(df.iat[0, 1]) # 101
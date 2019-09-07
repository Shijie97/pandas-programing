# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5, 4), index = list('12345'), columns = list('ABCD'))
print(df)

# loc，指定行列的内容来选定
# 下面两种方式等价，都是输出'A这一列'
print(df.loc[:, 'A'])
print(df['A'])

# 也可以只选中行
# 下面两种方式等价，都是输出index的内容为'1'的那一行
print(df.loc['1'])
print(df.loc['1', :])

# 自定义区域
print(df.loc[['2', '5'], ['A', 'D']])

# 可以筛选
print(df.loc['1'] > 0) # 返回index=1那一行每列是否大于0的布尔值
# A    True
# B    True
# C    True
# D    True
# Name: 1, dtype: bool

# 判断'A'这一列的每一行是否都大于0
print(df.loc[:, 'A'] > 0)
# 1    True
# 2    True
# 3    True
# 4    True
# 5    True
# Name: A, dtype: bool

# iloc，基于行列下标的索引
print(df.iloc[0]) # 默认的第一个数字为行，这行代码输出第一行
print(df.iloc[0, 0]) # 输出第一行第一个元素
print(df.iloc[:, 0]) # 输出'A'这一列
print(df.iloc[[0, 1], [0, 1]]) # 前两行的前两列

# 用中括号索引
# 下面两行等价
print(df['A']) # 输出'A'这一列
print(df.A)

# 中括号里面要索引行，只能用切片，其他方式都不行
print(df[:2]) # 输出前两行
# print(df[[0, 1]]) # 会报错
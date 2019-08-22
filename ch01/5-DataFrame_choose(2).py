# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.permutation(28).reshape(7, 4), index = np.random.permutation(np.arange(1, 8)), columns = list('BCDA'))
print(df)
print('--' * 20)

# loc[X]，表示获取行的内容为X的那一行
print(df.loc[1]) # 获取index为1的那一行
print('--' * 20)
print(df.loc[[5, 7]]) # 获取index为5和7的那两行
print('--' * 20)

# iloc[X]，表示获取index行号（不是内容，而是真正的下标）对应的那一行
print(df.iloc[6]) # 获取最后一行，因为总共就7行，下标为6就代表最后一行
print('--' * 20)
print(df.iloc[-1]) # 同理，-1也代表最后一行
print('--' * 20)
print(df.iloc[[-1, 0]]) # 获取最后一行以及第一行

# 可以同时指定行和列
print('--' * 20)
print(df.loc[[1, 5], ['A', 'D']]) # index的内容为1和5，输出列为A和D

# 加入一些表达式
print(df.loc[df['A'] == 0]) # 选择A这一列含有0的那些行
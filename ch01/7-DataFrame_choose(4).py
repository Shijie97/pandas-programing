# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.permutation(28).reshape(7, 4), index = np.random.permutation(np.arange(1, 8)), columns = list('BCDA'))
print(df)

print('-' * 15)

# 筛选出元素大于5的，小于等于5的变成NaN
print(df[df > 5])

# 筛选出B列元素在7~9之间的所有行
# 注意这里每个布尔表达式只能用最简单的形式，表示&关系
# 注意单个最简单的布尔表达式要用小括号单独括起来
print('-' * 15)
print(df[(df.B > 6) & ~(df.B < 10)]) # B这一列全部大于等于10

# 复制
df2 = df.copy() # 深复制
df2['E'] = list('abcdefg')
print('-' * 15)
print(df2)

# isin()函数
print('-' * 15)
print(df2[df2['E'].isin(['a', 'g'])]) # 选出E这一列为a和g的那两行
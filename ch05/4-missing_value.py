# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# isnull, notnull返回布尔值
s = pd.Series(np.array([1, 2, np.nan, 4]))
print(s.isnull())
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool

print(s.notnull())
# 0     True
# 1     True
# 2    False
# 3     True
# dtype: bool

# 求和运算时，NaN视为0，如果全部为NaN, 则答案仍为0
print(s.sum()) # 7.0

s2 = pd.Series([np.nan] * 5)
print(s2.sum()) # 0

# 用标量来填充NaN，用fillna
df = pd.DataFrame({'A' : s, 'B' : np.arange(4)})
# 重新指定索引值，0~3是原来的值，其他行一律为NaN
df = df.reindex(np.arange(0, 6))
print(df)
#      A    B
# 0  1.0  0.0
# 1  2.0  1.0
# 2  NaN  2.0
# 3  4.0  3.0
# 4  NaN  NaN
# 5  NaN  NaN
new_df = df.fillna(666)
print(new_df)
#        A      B
# 0    1.0    0.0
# 1    2.0    1.0
# 2  666.0    2.0
# 3    4.0    3.0
# 4  666.0  666.0
# 5  666.0  666.0

# pad表示正向填充，NaN为上一行的值
new_df = df.fillna(method = 'pad')
print(new_df)
#      A    B
# 0  1.0  0.0
# 1  2.0  1.0
# 2  2.0  2.0
# 3  4.0  3.0
# 4  4.0  3.0
# 5  4.0  3.0


# 为df添加一行，index为1000，A和B分别是100和101
df = df.append(pd.DataFrame([{'A' : 100, 'B' : 101}], index = [1000]))
print(df)
#           A      B
# 0       1.0    0.0
# 1       2.0    1.0
# 2       NaN    2.0
# 3       4.0    3.0
# 4       NaN    NaN
# 5       NaN    NaN
# 1000  100.0  101.0

# backfill为反向填充，NaN为下一行的值
new_df = df.fillna(method = 'backfill')
print(new_df)
#           A      B
# 0       1.0    0.0
# 1       2.0    1.0
# 2       4.0    2.0
# 3       4.0    3.0
# 4     100.0  101.0
# 5     100.0  101.0
# 1000  100.0  101.0

# dropna，默认axis = 0，即按轴删除，只要一行有NaN，就删除这一整行
print(df.dropna()) # 2 4 5行被删除了

#           A      B
# 0       1.0    0.0
# 1       2.0    1.0
# 3       4.0    3.0
# 1000  100.0  101.0

# 因为每列都有NaN，所以两列都被删除了
print(df.dropna(axis = 1))
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3, 4, 5, 1000]

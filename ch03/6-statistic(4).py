# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# pct_change用于显示这一行/列相对于上一行/列的变化百分比

df = pd.DataFrame(np.arange(1, 17).reshape(4, 4))
print(df)
#     0   1   2   3
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16
print(df.pct_change(axis = 0))
#           0         1         2         3
# 0       NaN       NaN       NaN       NaN
# 1  4.000000  2.000000  1.333333  1.000000
# 2  0.800000  0.666667  0.571429  0.500000
# 3  0.444444  0.400000  0.363636  0.333333
print(df.pct_change(axis = 1))
#     0         1         2         3
# 0 NaN  1.000000  0.500000  0.333333
# 1 NaN  0.200000  0.166667  0.142857
# 2 NaN  0.111111  0.100000  0.090909
# 3 NaN  0.076923  0.071429  0.066667

# cov返回协方差/协方差矩阵
s1 = pd.Series(np.arange(10))
s2 = pd.Series(reversed((np.arange(10))))
print(s1.cov(s2)) # -9.166666666666666

# 返回协方差矩阵，返回每列之间的协方差，构成一个协方差矩阵
# 先改变列名
dic = {list(df.columns)[i] : list('ABCD')[i] for i in np.arange(4)}
df = df.rename(columns = dic)
print(df)
#     A   B   C   D
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16

# 注意这里返回的是每列的协方差，不是每行的
print(df.cov())
#            A          B          C          D
# A  26.666667  26.666667  26.666667  26.666667
# B  26.666667  26.666667  26.666667  26.666667
# C  26.666667  26.666667  26.666667  26.666667
# D  26.666667  26.666667  26.666667  26.666667

# 返回相关性 corr
print(df.corr())
#      A    B    C    D
# A  1.0  1.0  1.0  1.0
# B  1.0  1.0  1.0  1.0
# C  1.0  1.0  1.0  1.0
# D  1.0  1.0  1.0  1.0
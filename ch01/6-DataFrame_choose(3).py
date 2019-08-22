# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.permutation(28).reshape(7, 4), index = np.random.permutation(np.arange(1, 8)), columns = list('BCDA'))
print(df)
print('-' * 15)

# at[]，用于获取指定行列内容对应的元素
print(df.at[2, 'B'])

# iat[]，用于获取指定行列序号下标对应的元素
print(df.iat[0, 0])

#     B   C   D   A
# 5   3   5   2   7
# 4  16  15  14  19
# 2  22  13  18  27
# 1  20   4  25  26
# 7  12   1  24   9
# 3   6  10  11  21
# 6  23  17   0   8
# ---------------
# 22
# 3

# 还可以改变某一个元素
df.iat[0, 0] = 666
print('-' * 15)
print(df)

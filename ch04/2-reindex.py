# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

N = 20

df = pd.DataFrame({
    'A' : pd.date_range(start = '20190825', periods = N),
    'B' : np.linspace(0, N-1, N),
    'C' : np.random.rand(N),
    'D' : np.random.choice(['low', 'middle', 'high'], N),
    'E' : np.random.normal(100, 10, N)
})

print(df)
#             A     B         C       D           E
# 0  2019-08-25   0.0  0.163282     low   79.371747
# 1  2019-08-26   1.0  0.014611     low  101.117914
# 2  2019-08-27   2.0  0.448706  middle   93.353039
# 3  2019-08-28   3.0  0.579925  middle   97.043347
# 4  2019-08-29   4.0  0.600001    high   89.586822
# 5  2019-08-30   5.0  0.247754     low  100.077992
# 6  2019-08-31   6.0  0.291771  middle   97.935353
# 7  2019-09-01   7.0  0.280156     low   99.889177
# 8  2019-09-02   8.0  0.407803  middle  102.270114
# 9  2019-09-03   9.0  0.124462     low  101.018815
# 10 2019-09-04  10.0  0.980287  middle   96.484679
# 11 2019-09-05  11.0  0.678561     low   96.332807
# 12 2019-09-06  12.0  0.485492  middle  110.718751
# 13 2019-09-07  13.0  0.220921  middle   99.583902
# 14 2019-09-08  14.0  0.188073     low  100.466108
# 15 2019-09-09  15.0  0.748863     low   88.035008
# 16 2019-09-10  16.0  0.284103    high  118.746508
# 17 2019-09-11  17.0  0.639313     low  113.948363
# 18 2019-09-12  18.0  0.371002    high  101.876442
# 19 2019-09-13  19.0  0.758376  middle   75.203701


# 重建索引可以只提取出有用的数据
df_reindex = df.reindex(index = [0, 2, 5], columns = ['A', 'D'])
print(df_reindex)
# 0 2019-08-25     low
# 2 2019-08-27  middle
# 5 2019-08-30     low

df1 = pd.DataFrame(np.random.permutation(np.arange(16)).reshape(4, 4), columns = ['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.permutation(np.arange(20)).reshape(5, 4), columns = ['A', 'B', 'C', 'D'])
print(df1)
#     A   B   C   D
# 0   1   8  12  10
# 1  15   0   6   5
# 2  11   4   3   7
# 3  13  14   9   2
print(df2)
#     A   B   C   D
# 0  18   6  10   8
# 1   7   9  15   4
# 2   5   3  17  14
# 3  16  19   2  11
# 4   1  13  12   0


# reindex_like，将df2的index和df1保持一致，即0123而不是01234，对应为前四行
df2 = df2.reindex_like(df1)
print(df2)
#     A   B   C   D
# 0  18   6  10   8
# 1   7   9  15   4
# 2   5   3  17  14
# 3  16  19   2  11

# 重建索引时可以填充
df3 = pd.DataFrame(np.random.permutation(np.arange(32)).reshape(8, 4), columns = ['A', 'B', 'C', 'D'])

# 如果不填充
df1 = df1.reindex_like(df3)
print('=' * 15 + '不填充' + '=' * 15)
print(df1)
#       A     B     C     D
# 0  14.0   5.0   6.0  12.0
# 1  13.0   7.0   1.0   2.0
# 2   0.0   3.0   4.0  11.0
# 3   8.0  10.0  15.0   9.0
# 4   NaN   NaN   NaN   NaN
# 5   NaN   NaN   NaN   NaN
# 6   NaN   NaN   NaN   NaN
# 7   NaN   NaN   NaN   NaN

# 如果填充
df1 = df1.head(4)
df1 = df1.reindex_like(df3, method = 'pad')
print('=' * 15 + '填充' + '=' * 15)
print(df1)
#       A     B     C     D
# 0  14.0   5.0   6.0  12.0
# 1  13.0   7.0   1.0   2.0
# 2   0.0   3.0   4.0  11.0
# 3   8.0  10.0  15.0   9.0
# 4   8.0  10.0  15.0   9.0
# 5   8.0  10.0  15.0   9.0
# 6   8.0  10.0  15.0   9.0
# 7   8.0  10.0  15.0   9.0

# 如果是带有限制的填充
df1 = df1.head(4)
df1 = df1.reindex_like(df3, method = 'ffill', limit = 1)
print('=' * 15 + '填充并带有限制' + '=' * 15)
print(df1)
#       A     B     C     D
# 0  12.0   7.0   1.0   5.0
# 1   6.0  13.0   4.0   0.0
# 2   3.0   2.0   8.0  10.0
# 3   9.0  14.0  15.0  11.0
# 4   9.0  14.0  15.0  11.0
# 5   NaN   NaN   NaN   NaN
# 6   NaN   NaN   NaN   NaN
# 7   NaN   NaN   NaN   NaN

# rename，用一个字典来重新命名index和col的名字
df = pd.DataFrame(np.random.permutation(np.arange(32)).reshape(8, 4), columns = ['A', 'B', 'C', 'D'])
dict_index = {i : i + 1 for i in range(df.shape[0])}
dict_col = {i : str.lower(i) for i in df.columns.values.tolist()}

print(dict_index)
# {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8}

print(dict_col)
# {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

df = df.rename(index = dict_index, columns = dict_col)
print(df)
#     a   b   c   d
# 1  18   7  21   3
# 2  10  22  27  12
# 3  26  17  23  11
# 4   5  15  20   8
# 5  16   1  28   2
# 6  14  31   4   6
# 7   0  30  13   9
# 8  19  25  24  29
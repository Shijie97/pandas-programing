# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df_unsorted = pd.DataFrame(np.random.permutation(np.arange(1, 25)).reshape(6, 4),
                           index = np.random.permutation(6),
                           columns= np.random.permutation(list('ABCD')))
print(df_unsorted)

#     D   B   C   A
# 1  21  10   3  11
# 3   9  12  14   1
# 0  23  18  22  13
# 2  24   6   2  17
# 5   8   5  19  15
# 4  20  16   7   4

# 按索引名字排序
# axis = 0表示对index名字进行排序
# 降序
df_sort_by_index_name = df_unsorted.sort_index(axis = 0, ascending = False)
print(df_sort_by_index_name)
#     D   B   C   A
# 5   8   5  19  15
# 4  20  16   7   4
# 3   9  12  14   1
# 2  24   6   2  17
# 1  21  10   3  11
# 0  23  18  22  13

# 按列名排序
df_sort_by_col_name = df_unsorted.sort_index(axis = 1)
print(df_sort_by_col_name)
#     A   B   C   D
# 1  11  10   3  21
# 3   1  12  14   9
# 0  13  18  22  23
# 2  17   6   2  24
# 5  15   5  19   8
# 4   4  16   7  20
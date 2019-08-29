# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np


# sort_values，以行为整体单位进行排序
# 排序标准为by后面接的列名

df_unsorted = pd.DataFrame(np.random.permutation(np.arange(1, 25)).reshape(6, 4),
                           index = np.random.permutation(6),
                           columns= np.random.permutation(list('ABCD')))
print(df_unsorted)
#     A   D   C   B
# 3  10  23  14   4
# 4  24  15  11   6
# 0  18   8   2  17
# 1   3  20  19   1
# 2   5  12   9   7
# 5  22  16  21  13

# by 后面接若干个列名，如果有相同的，继续看下一个列名
df_sorted = df_unsorted.sort_values(by = ['C', 'D'], ascending = [False, True])
print(df_sorted)
#     A   D   C   B
# 5  22  16  21  13
# 1   3  20  19   1
# 3  10  23  14   4
# 4  24  15  11   6
# 2   5  12   9   7
# 0  18   8   2  17
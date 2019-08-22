# !user/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.permutation(28).reshape(7, 4), index = np.random.permutation(np.arange(1, 8)), columns = list('BCDA'))
print(df)
print('--' * 20)

# sort_index，根据行标签和列标签进行排序
# axis = 0为按行排列，为1位按列排列
# ascending = True表示升序
print(df.sort_index(axis = 0, ascending = False)) # 按行排列，降序
print('--' * 20)
print(df.sort_index(axis = 1, ascending = True)) # 按列排列，升序
print('--' * 20)
# sort_values，按值排序
print(df.sort_values(axis = 0, by = 'B', ascending = False)) # 一定要注明axis，根据B那一列降序
print('--' * 20)
print(df.sort_values(axis = 0, by = ['B', 'C'], ascending = [True, False])) # 先按B升序，如果一样，就按C降序
#     B   C   D   A
# 2   5   2  23   8
# 3  18  21  13  10
# 4   9   6  11   3
# 1  25   0  27   4
# 7  19   1  12  26
# 5   7  24  14  16
# 6  15  17  20  22
# ----------------------------------------
#     B   C   D   A
# 7  19   1  12  26
# 6  15  17  20  22
# 5   7  24  14  16
# 4   9   6  11   3
# 3  18  21  13  10
# 2   5   2  23   8
# 1  25   0  27   4
# ----------------------------------------
#     A   B   C   D
# 2   8   5   2  23
# 3  10  18  21  13
# 4   3   9   6  11
# 1   4  25   0  27
# 7  26  19   1  12
# 5  16   7  24  14
# 6  22  15  17  20
# ----------------------------------------
#     B   C   D   A
# 1  25   0  27   4
# 7  19   1  12  26
# 3  18  21  13  10
# 6  15  17  20  22
# 4   9   6  11   3
# 5   7  24  14  16
# 2   5   2  23   8
# ----------------------------------------
#     B   C   D   A
# 2   5   2  23   8
# 5   7  24  14  16
# 4   9   6  11   3
# 6  15  17  20  22
# 3  18  21  13  10
# 7  19   1  12  26
# 1  25   0  27   4
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# 显式地创建Categorical数据

cg = pd.Categorical(['Role', 'Role', 'Star', 'Role', 'Killer', 'Star'], categories = ['Role', 'Star'])
print(cg)
# [Role, Role, Star, Role, NaN, Star]
# Categories (2, object): [Role, Star]

print(type(cg))
# <class 'pandas.core.arrays.categorical.Categorical'>

df = pd.DataFrame(np.arange(24).reshape(6, 4))
print(df)
#     0   1   2   3
# 0   0   1   2   3
# 1   4   5   6   7
# 2   8   9  10  11
# 3  12  13  14  15
# 4  16  17  18  19
# 5  20  21  22  23

# Categorical类型可以作为单独的一列
df['add'] = cg
print(df)
#     0   1   2   3   add
# 0   0   1   2   3  Role
# 1   4   5   6   7  Role
# 2   8   9  10  11  Star
# 3  12  13  14  15  Role
# 4  16  17  18  19   NaN
# 5  20  21  22  23  Star
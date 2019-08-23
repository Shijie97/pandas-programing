# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 查找系列数据

s = pd.Series(list('abcdef'), index = np.arange(6))
print(s[2]) # c

# 查找下标为0~3的元素
print(s[:4])

# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object

# 查找最后三个元素
# 这里和python不一样，注意甄别
print(s[-3:])

# 3    d
# 4    e
# 5    f
# dtype: object

# 使用索引标签值查找
s = pd.Series(np.arange(5), index = list('abcde'))
print(s['c']) # 2

# 查找多个元素
# 注意这里里面需要单独组成一个list
print(s[['c', 'e']])

# c    2
# e    4
# dtype: int32
# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 创建一个空系列
s = pd.Series()
print(s) # Series([], dtype: float64)

# 从ndarray创建一个系列
# 不指定index默认为np.arange(n)
data = np.array(list('abcd'))
s = pd.Series(data)
print(s)

# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object

# 指定index
s = pd.Series(data, index = np.arange(100, 100 + 4))
print(s)

# 100    a
# 101    b
# 102    c
# 103    d
# dtype: object

# 从字典创建系列
# key为index，value为具体值
dic = {'a' : 1, 'b' : 2, 'c' : 3}
s = pd.Series(dic)
print(s)

# a    1
# b    2
# c    3
# dtype: int64

# 对于字典构建系列，如果强行加上index呢？
# d和x找不到指定的值，所以为NaN，而且强行指定的b对应的字典中的b
s = pd.Series(dic, index = ['b', 'c', 'd', 'a', 'x'])
print(s)

# b    2.0
# c    3.0
# d    NaN
# a    1.0
# x    NaN
# dtype: float64

# 从标量创建一个序列
s = pd.Series(5, index = np.arange(4))
print(s)

# 0    5
# 1    5
# 2    5
# 3    5
# dtype: int64

#
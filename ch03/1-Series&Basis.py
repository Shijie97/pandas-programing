# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

data = np.random.rand(4)
s = pd.Series(data)
print(s)

# 0    0.568146
# 1    0.899250
# 2    0.031503
# 3    0.241778
# dtype: float64

# axes，返回行轴标签列表
print(s.axes)
# [RangeIndex(start=0, stop=4, step=1)]

# empty，判断是否为空
print(s.empty) # False

# ndim 返回维度
# Series注定是一维的
print(s.ndim) # 1

# size，返回长度，即元素个数
print(s.size) # 4

# values，以数组的形式返回元素的具体值
print(s.values) # [0.27071307 0.07339438 0.69003613 0.28399415]

# head(n)，返回前n行
print(s.head(2))

# 0    0.681181
# 1    0.467637
# dtype: float64

# tail(n)，返回后n行
print(s.tail(2))

# 2    0.278933
# 3    0.780957
# dtype: float64
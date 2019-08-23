# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 数据帧的创建

# 创建一个空的数据帧
df = pd.DataFrame()
print(df)

# Empty DataFrame
# Columns: []
# Index: []

# 从列表创建数据帧
# 不指定index和col，默认均为np.arange(n)
df = pd.DataFrame(np.arange(5))
print(df)

#    0
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4

# 当列表为二维
data = np.array([['zsj', 22],
                 ['yaoming', 40],
                 ['xiaoming', 12]])
df = pd.DataFrame(data, columns = ['name', 'age'])
print(df)

#        name age
# 0       zsj  22
# 1   yaoming  40
# 2  xiaoming  12

# 从list/ndarray为value的字典创建数据帧
dic = {'name' : ['zsj', 'yaoming', 'xiaoming'],
       'age' : [22, 40, 12]}
df = pd.DataFrame(dic)
print(df)

#        name  age
# 0       zsj   22
# 1   yaoming   40
# 2  xiaoming   12

# 指定index
df = pd.DataFrame(dic, index = np.arange(100, 100 + 3))
print(df)

#          name  age
# 100       zsj   22
# 101   yaoming   40
# 102  xiaoming   12
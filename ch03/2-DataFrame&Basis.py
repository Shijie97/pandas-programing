# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print(df)

#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Minsu   29    4.60
# 6   Jack   23    3.80

# T，行列互换
print(df.T)

#            0      1      2     3      4      5     6
# Name     Tom  James  Ricky   Vin  Steve  Minsu  Jack
# Age       25     26     25    23     30     29    23
# Rating  4.23   3.24   3.98  2.56    3.2    4.6   3.8

# axes，返回行轴和列轴的标签列表
# 先显示index，再显示col
print(df.axes)
# [RangeIndex(start=0, stop=7, step=1), Index(['Name', 'Age', 'Rating'], dtype='object')]

# dtypes，返回每列的数据类型
print(df.dtypes)

# Name       object
# Age         int64
# Rating    float64
# dtype: object

# empty，返回是否为空
print(df.empty) # False

# ndim，返回维度
print(df.ndim) # 2

# shape，返回形状
print(df.shape) # (7, 3)

# size，返回元素总个数
print(df.size) # 21

# values，返回data，以ndarray的二维数组的形式返回
print(df.values)

# [['Tom' 25 4.23]
#  ['James' 26 3.24]
#  ['Ricky' 25 3.98]
#  ['Vin' 23 2.56]
#  ['Steve' 30 3.2]
#  ['Minsu' 29 4.6]
#  ['Jack' 23 3.8]]

# head，返回前n行
print(df.head(3))

#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98

# tail，返回后n行
print(df.tail(2))

#     Name  Age  Rating
# 5  Minsu   29     4.6
# 6   Jack   23     3.8
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df)

# 常用函数
# count() 非空元素数量
# sum() 求和
# mean() 平均数
# median() 中位数
# mode() 众数
# std() 标准差
# min() 最小值
# max() 最大值
# abs() 绝对值
# prod() 乘积
# cumsum() 累计总和
# cumprod() 累计乘积

# 下面挑几个不熟悉的讲一下

# mode
# numeric_only = True表示仅对数值的行/列进行求众数，默认为False
print(df.mode(axis = 0, numeric_only = True))

# 解释一下下面这个图，Rating的众数有12个，因此有12行，Age的众数有三个，NaN表示没有
#      Age  Rating
# 0   23.0    2.56
# 1   25.0    2.98
# 2   30.0    3.20
# 3    NaN    3.24
# 4    NaN    3.65
# 5    NaN    3.78
# 6    NaN    3.80
# 7    NaN    3.98
# 8    NaN    4.10
# 9    NaN    4.23
# 10   NaN    4.60
# 11   NaN    4.80

# abs绝对值，abs返回一个DataFrame
# abs不允许某列是非数字，因此我先把带有字符串的两列删了，再增加一列负的
del df['Age']
del df['Name']
df['-Rating'] = -df['Rating']
print(df)
#     Rating  -Rating
# 0     4.23    -4.23
# 1     3.24    -3.24
# 2     3.98    -3.98
# 3     2.56    -2.56
# 4     3.20    -3.20
# 5     4.60    -4.60
# 6     3.80    -3.80
# 7     3.78    -3.78
# 8     2.98    -2.98
# 9     4.80    -4.80
# 10    4.10    -4.10
# 11    3.65    -3.65

print(df.abs())
#     Rating  -Rating
# 0     4.23     4.23
# 1     3.24     3.24
# 2     3.98     3.98
# 3     2.56     2.56
# 4     3.20     3.20
# 5     4.60     4.60
# 6     3.80     3.80
# 7     3.78     3.78
# 8     2.98     2.98
# 9     4.80     4.80
# 10    4.10     4.10
# 11    3.65     3.65

# prod
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
df['col5'] = pd.Series([2] * 12)
print(df.prod())

# Age       7.158408e+17
# Rating    6.320128e+06
# col5      4.096000e+03 4096 = 2 ** 12
# dtype: float64

# cumsum 累加，返回一个DataFrame
print(df.cumsum()) # 默认为 axis = 0
#                                                  Name  Age Rating col5
# 0                                                 Tom   25   4.23    2
# 1                                            TomJames   51   7.47    4
# 2                                       TomJamesRicky   76  11.45    6
# 3                                    TomJamesRickyVin   99  14.01    8
# 4                               TomJamesRickyVinSteve  129  17.21   10
# 5                          TomJamesRickyVinSteveMinsu  158  21.81   12
# 6                      TomJamesRickyVinSteveMinsuJack  181  25.61   14
# 7                   TomJamesRickyVinSteveMinsuJackLee  215  29.39   16
# 8              TomJamesRickyVinSteveMinsuJackLeeDavid  255  32.37   18
# 9        TomJamesRickyVinSteveMinsuJackLeeDavidGasper  285  37.17   20
# 10  TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...  336  41.27   22
# 11  TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...  382  44.92   2

# cumprod 累乘
# 字符串可以相加，但是不能相乘，所以先删掉字符串那一列
df.pop('Name')
print(df.cumprod())
#              Age        Rating    col5
# 0   2.500000e+01  4.230000e+00     2.0
# 1   6.500000e+02  1.370520e+01     4.0
# 2   1.625000e+04  5.454670e+01     8.0
# 3   3.737500e+05  1.396395e+02    16.0
# 4   1.121250e+07  4.468465e+02    32.0
# 5   3.251625e+08  2.055494e+03    64.0
# 6   7.478738e+09  7.810877e+03   128.0
# 7   2.542771e+11  2.952512e+04   256.0
# 8   1.017108e+13  8.798485e+04   512.0
# 9   3.051325e+14  4.223273e+05  1024.0
# 10  1.556176e+16  1.731542e+06  2048.0
# 11  7.158408e+17  6.320128e+06  4096.0
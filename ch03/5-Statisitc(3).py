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
#       Name  Age  Rating
# 0      Tom   25    4.23
# 1    James   26    3.24
# 2    Ricky   25    3.98
# 3      Vin   23    2.56
# 4    Steve   30    3.20
# 5    Minsu   29    4.60
# 6     Jack   23    3.80
# 7      Lee   34    3.78
# 8    David   40    2.98
# 9   Gasper   30    4.80
# 10  Betina   51    4.10
# 11  Andres   46    3.65

# describe返回每一列的摘要
print(df.describe())

#              Age     Rating
# count  12.000000  12.000000
# mean   31.833333   3.743333
# std     9.232682   0.661628
# min    23.000000   2.560000
# 25%    25.000000   3.230000
# 50%    29.500000   3.790000
# 75%    35.500000   4.132500
# max    51.000000   4.800000

# describe默认参数为 include = 'number'，即默认只关心数字那一栏
# 参数可选有，number、object、all，分别对应数字、字符串和所有
print(df.describe(include = 'object'))

#          Name
# count      12
# unique     12
# top     Steve
# freq        1

print(df.describe(include = 'all'))

#        Name        Age     Rating
# count    12  12.000000  12.000000
# unique   12        NaN        NaN
# top     Tom        NaN        NaN
# freq      1        NaN        NaN
# mean    NaN  31.833333   3.743333
# std     NaN   9.232682   0.661628
# min     NaN  23.000000   2.560000
# 25%     NaN  25.000000   3.230000
# 50%     NaN  29.500000   3.790000
# 75%     NaN  35.500000   4.132500
# max     NaN  51.000000   4.800000
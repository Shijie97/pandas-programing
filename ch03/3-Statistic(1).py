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

# sum，默认求所有列的总和
print(df.sum()) # 默认为axis = 0

# Name      TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...
# Age                                                     382
# Rating                                                44.92
# dtype: object

print(df.sum(axis = 1)) # 求每一行数字的和

# 0     29.23
# 1     29.24
# 2     28.98
# 3     25.56
# 4     33.20
# 5     33.60
# 6     26.80
# 7     37.78
# 8     42.98
# 9     34.80
# 10    55.10
# 11    49.65
# dtype: float64

# 完整形式
print(df.sum(axis = 0))

# Name      TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...
# Age                                                     382
# Rating                                                44.92
# dtype: object

# mean，默认axis = 0，且只针对有数的列
print(df.mean())
# Age       31.833333
# Rating     3.743333
# dtype: float64

# 每行求平均值
print(df.mean(axis = 1))

# 0     14.615
# 1     14.620
# 2     14.490
# 3     12.780
# 4     16.600
# 5     16.800
# 6     13.400
# 7     18.890
# 8     21.490
# 9     17.400
# 10    27.550
# 11    24.825
# dtype: float64

# std，标准差
# 同理，啥也不写默认axis = 0
print(df.std())

# Age       9.232682
# Rating    0.661628
# dtype: float64

# 每行标准差
print(df.std(axis = 1))
# 0     14.686608
# 1     16.093750
# 2     14.863385
# 3     14.453263
# 4     18.950462
# 5     17.253405
# 6     13.576450
# 7     21.368767
# 8     26.177093
# 9     17.819091
# 10    33.163308
# 11    29.945972
# dtype: float64


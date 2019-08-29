# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

print(df)
#             A     x         y       C           D
# 0  2016-01-01   0.0  0.897499  Medium   97.652534
# 1  2016-01-02   1.0  0.498053  Medium   93.772434
# 2  2016-01-03   2.0  0.320607  Medium  106.588819
# 3  2016-01-04   3.0  0.081239    High   99.627237
# 4  2016-01-05   4.0  0.001076     Low  107.882239
# 5  2016-01-06   5.0  0.510186     Low  101.773385
# 6  2016-01-07   6.0  0.220431     Low   95.179603
# 7  2016-01-08   7.0  0.697727    High   79.481735
# 8  2016-01-09   8.0  0.414487  Medium  116.819987
# 9  2016-01-10   9.0  0.053145    High   97.704548
# 10 2016-01-11  10.0  0.772597  Medium  105.862849
# 11 2016-01-12  11.0  0.522089    High  120.881666
# 12 2016-01-13  12.0  0.208383    High   99.920382
# 13 2016-01-14  13.0  0.843192  Medium  110.208575
# 14 2016-01-15  14.0  0.090102  Medium  117.888005
# 15 2016-01-16  15.0  0.147771    High  108.069190
# 16 2016-01-17  16.0  0.896215     Low   99.130472
# 17 2016-01-18  17.0  0.584072  Medium   89.179121
# 18 2016-01-19  18.0  0.159581    High  106.861453
# 19 2016-01-20  19.0  0.282911     Low   86.076621

# 遍历每个列名
for col in df:
    print(col)

# iteritems()函数，针对每一列，k为列名，v为Series，对应那一列
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for k, v in df.iteritems():
    print(k)
    print('-' * 20)
    print(v)
    print(type(v)) # <class 'pandas.core.series.Series'>

# col1
# --------------------
# 0    0.147206
# 1   -1.281577
# 2   -0.928580
# 3   -1.476905
# Name: col1, dtype: float64
# col2
# --------------------
# 0   -2.255746
# 1    0.346670
# 2   -1.338567
# 3   -0.526141
# Name: col2, dtype: float64
# col3
# --------------------
# 0    1.950712
# 1   -0.694341
# 2   -0.250373
# 3    0.722871
# Name: col3, dtype: float64

# iterrows()针对每一行，k为行号名，v为Series，为那行的元素
for k, v in df.iterrows():
    print(k)
    print('-' * 20)
    print(v)
    print(type(v))

# 0
# col1    0.430952
# col2    0.270875
# col3    0.282953
# Name: 0, dtype: float64
# <class 'pandas.core.series.Series'>
# 1
# --------------------
# col1    0.392221
# col2   -0.562287
# col3    0.903608
# Name: 1, dtype: float64
# <class 'pandas.core.series.Series'>
# 2
# --------------------
# col1    2.256837
# col2   -0.689041
# col3   -0.720947
# Name: 2, dtype: float64
# <class 'pandas.core.series.Series'>
# 3
# --------------------
# col1    0.024497
# col2    0.526463
# col3    2.044937
# Name: 3, dtype: float64
# <class 'pandas.core.series.Series'>

# itertupules()针对每一行，返回一个<class 'pandas.core.frame.Pandas'>类型的元组
# 元组的第一个元素为index名字，后面分别是改行每一列的具体内容
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print (row)
    print(type(row))
    print(tuple(row))

# Pandas(Index=0, col1=0.6931639945070625, col2=0.47316739867164104, col3=0.6357804282938343)
# Pandas(Index=1, col1=0.07939910162780936, col2=0.29306780681533057, col3=0.337999647976845)
# Pandas(Index=2, col1=-1.1546934499927561, col2=0.83784074710708, col3=-0.7315030470803993)
# Pandas(Index=3, col1=0.585248125350287, col2=1.0220965245068494, col3=0.3011521493149711)
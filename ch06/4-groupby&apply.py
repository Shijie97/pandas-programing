# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.read_excel('sales_transactions.xlsx')
print(df)
#     account           name  order       sku  quantity  unit price  ext price
# 0    383080       Will LLC  10001  B1-20000         7       33.69     235.83
# 1    383080       Will LLC  10001  S1-27722        11       21.12     232.32
# 2    383080       Will LLC  10001  B1-86481         3       35.99     107.97
# 3    412290  Jerde-Hilpert  10005  S1-06532        48       55.82    2679.36
# 4    412290  Jerde-Hilpert  10005  S1-82801        21       13.62     286.02
# 5    412290  Jerde-Hilpert  10005  S1-06532         9       92.55     832.95
# 6    412290  Jerde-Hilpert  10005  S1-47412        44       78.91    3472.04
# 7    412290  Jerde-Hilpert  10005  S1-27722        36       25.42     915.12
# 8    218895      Kulas Inc  10006  S1-27722        32       95.66    3061.12
# 9    218895      Kulas Inc  10006  B1-33087        23       22.55     518.65
# 10   218895      Kulas Inc  10006  B1-33364         3       72.30     216.90
# 11   218895      Kulas Inc  10006  B1-20000        -1       72.18     -72.18

# apply可以对多个列进行操作，返回的也可以不是标量，而是向量
# 方法一
def add(x): # 这里的x指的是整个数据帧
    return x['quantity'] + x['unit price']

print(df.groupby('order').apply(add)) # apply的第一个形参是self，传入的是分好后的每组
# order
# 10001  0      40.69
#        1      32.12
#        2      38.99
# 10005  3     103.82
#        4      34.62
#        5     101.55
#        6     122.91
#        7      61.42
# 10006  8     127.66
#        9      45.55
#        10     75.30
#        11     71.18
# dtype: float64

print('-' * 20)

# 方法二
print(df.groupby('order').apply(lambda x : x['quantity'] + x['unit price']))

# order
# 10001  0      40.69
#        1      32.12
#        2      38.99
# 10005  3     103.82
#        4      34.62
#        5     101.55
#        6     122.91
#        7      61.42
# 10006  8     127.66
#        9      45.55
#        10     75.30
#        11     71.18
# dtype: float64

print('-' * 100)

print(df.groupby('order', group_keys = False).apply(lambda x : x['quantity'] + x['unit price']))
# 0      40.69
# 1      32.12
# 2      38.99
# 3     103.82
# 4      34.62
# 5     101.55
# 6     122.91
# 7      61.42
# 8     127.66
# 9      45.55
# 10     75.30
# 11     71.18
# dtype: float64

# 如果用apply返回标量，和agg还是有一定的区别
# apply是对每一列求标量，包括分组那一列
print(df.groupby('order').apply(np.min))
#        account           name  order       sku  quantity  unit price  ext price
# order
# 10001   383080       Will LLC  10001  B1-20000         3       21.12     107.97
# 10005   412290  Jerde-Hilpert  10005  S1-06532         9       13.62     286.02
# 10006   218895      Kulas Inc  10006  B1-20000        -1       22.55     -72.18

# 而agg是对除了分组之外的其他所有求标量
print(df.groupby('order').aggregate(np.min))
#        account           name       sku  quantity  unit price  ext price
# order
# 10001   383080       Will LLC  B1-20000         3       21.12     107.97
# 10005   412290  Jerde-Hilpert  S1-06532         9       13.62     286.02
# 10006   218895      Kulas Inc  B1-20000        -1       22.55     -72.18

# 两者都可以指定同一列求标量
print(df.groupby('order')['ext price'].apply(np.min))
# order
# 10001    107.97
# 10005    286.02
# 10006    -72.18
# Name: ext price, dtype: float64

print(df.groupby('order')['ext price'].aggregate(np.min))
# order
# 10001    107.97
# 10005    286.02
# 10006    -72.18
# Name: ext price, dtype: float64
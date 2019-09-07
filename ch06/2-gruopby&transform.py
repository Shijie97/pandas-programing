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

# 现在我要查看每个订单的总花费，并且还要计算各个订单的花费占该订单总花费的百分比，并额外添加一列，咋整？

# transform返回和原数据帧相同行数的数据帧，且只有一列，即shape为(len(df), 1)
# 这一列，相同组的元素都是一样的，都是求的该组的ext price的和
print(df.groupby('order')['ext price'].transform(np.sum))
# 0      576.12
# 1      576.12
# 2      576.12
# 3     8185.49
# 4     8185.49
# 5     8185.49
# 6     8185.49
# 7     8185.49
# 8     3724.49
# 9     3724.49
# 10    3724.49
# 11    3724.49
# Name: ext price, dtype: float64

# aggregate方法只能对某一列进行操作，返回的结果必须是标量，即一个数，比如求和啦，极差啦
# 返回的时候包括组名和对应组的操作结果
print(df.groupby('order')['ext price'].aggregate(np.sum))
# order
# 10001     576.12
# 10005    8185.49
# 10006    3724.49
# Name: ext price, dtype: float64

# apply可以对一列或者多列进行操作，返回的结果是标量或者是向量，比较灵活
print(df.groupby('order')['ext price'].apply(np.sum))
# order
# 10001     576.12
# 10005    8185.49
# 10006    3724.49
# Name: ext price, dtype: float64


# 有了transform，就可以比较轻松的进行求比例的问题了
df['per_of_order'] = df['ext price'] / df.groupby('order')['ext price'].transform(np.sum)
print(df['per_of_order'])
# 0     0.409342
# 1     0.403249
# 2     0.187409
# 3     0.327330
# 4     0.034942
# 5     0.101759
# 6     0.424170
# 7     0.111798
# 8     0.821890
# 9     0.139254
# 10    0.058236
# 11   -0.019380
# Name: per_of_order, dtype: float64

print(df.groupby('order')['ext price'].transform(lambda x : x - np.mean(x)))
# print(df.groupby('order')['ext price'].aggregate(lambda x : x - np.mean(x)) # 报错
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1, 17).reshape(8, 2), columns = ['A', 'B'])
print(df)
#     A   B
# 0   1   2
# 1   3   4
# 2   5   6
# 3   7   8
# 4   9  10
# 5  11  12
# 6  13  14
# 7  15  16
r = df.rolling(window = 3, min_periods = 1)

print(r)
# Rolling [window=3,min_periods=1,center=False,axis=0]

# aggregate，在rolling、expanding和ewm的基础上进行聚合
# 相当于在rolling的基础上进行一个求和运算，window为3，说明只关心最近三天的
# 但是min_periods = 1，因此哪怕不够三天，只有一天也可以求，所以前两行不是NaN而是具体的数
print(r.aggregate(np.sum)) # 等价于print(r.sum())，只不过这种写法更高级，可以玩出花来
#       A     B
# 0   1.0   2.0
# 1   4.0   6.0
# 2   9.0  12.0
# 3  15.0  18.0
# 4  21.0  24.0
# 5  27.0  30.0
# 6  33.0  36.0
# 7  39.0  42.0

print('-' * 20)
print(r.sum())
#       A     B
# 0   1.0   2.0
# 1   4.0   6.0
# 2   9.0  12.0
# 3  15.0  18.0
# 4  21.0  24.0
# 5  27.0  30.0
# 6  33.0  36.0
# 7  39.0  42.0


# 可以指定列
print(r['B'].aggregate(np.sum))
# 0     2.0
# 1     6.0
# 2    12.0
# 3    18.0
# 4    24.0
# 5    30.0
# 6    36.0
# 7    42.0
# Name: B, dtype: float64

# 可以指定多个函数
# 对B这一列，分别求近三天的和，以及近三天的平均值
print(r['B'].aggregate([np.sum, np.mean]))
#     sum  mean
# 0   2.0   2.0
# 1   6.0   3.0
# 2  12.0   4.0
# 3  18.0   6.0
# 4  24.0   8.0
# 5  30.0  10.0
# 6  36.0  12.0
# 7  42.0  14.0

# 还可以不同的列，对应不同的函数
# 对A列，求最近三天的和，对B列，求最近三天的平均值
print(r.aggregate({'A' : np.sum, 'B' : np.mean}))
#       A     B
# 0   1.0   2.0
# 1   4.0   3.0
# 2   9.0   4.0
# 3  15.0   6.0
# 4  21.0   8.0
# 5  27.0  10.0
# 6  33.0  12.0
# 7  39.0  14.0
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# 要将自定义函数作用于，DataFrame，即将其作为函数参数分为三种情况
# 1. 作用于整个表格 -> pipe()
# 2. 作用于行或列 -> apply()
# 3. 作用于某一个元素 -> applymap()

# 第一类
# 表格函数应用，即函数将作用于整个表格
# e.g. 为数据帧所有元素 + 2

# 先定义函数
def adder(ele1, ele2):
    return ele1 + ele2

df = pd.DataFrame(np.arange(1, 25).reshape(6, 4), columns = list('ABCD'))
print(df)
#     A   B   C   D
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16
# 4  17  18  19  20
# 5  21  22  23  24
new_df = df.pipe(adder, 2) # 后面只用接一个参数，因为第一个参数已经有了，就是df本身
print(new_df)
#     A   B   C   D
# 0   3   4   5   6
# 1   7   8   9  10
# 2  11  12  13  14
# 3  15  16  17  18
# 4  19  20  21  22
# 5  23  24  25  26

# 本来要这么写，但是用pipe之后就有点链式编程的味道
new_df2 = adder(df, 2)
print(new_df2)

#     A   B   C   D
# 0   3   4   5   6
# 1   7   8   9  10
# 2  11  12  13  14
# 3  15  16  17  18
# 4  19  20  21  22
# 5  23  24  25  26

# 第二类
# 行和列函数应用
# 比如我要把numpy的mean函数应用到数据帧中
# 应用apply的时候，默认为对列进行操作，如需更改，请改变axis
print(df.apply(np.mean, axis = 0)) # mean，每一列的
# A    11.0
# B    12.0
# C    13.0
# D    14.0
# dtype: float64

print(df.apply(np.mean, axis = 1)) # mean，每一行的
# 0     2.5
# 1     6.5
# 2    10.5
# 3    14.5
# 4    18.5
# 5    22.5
# dtype: float64

# 另外一个例子，求每列极差
print(df.apply(lambda x : np.max(x) - np.min(x), axis = 0))
# A    20
# B    20
# C    20
# D    20
# dtype: int64

# 求每行极差
print(df.apply(lambda x : np.max(x) - np.min(x), axis = 1))
# 0    3
# 1    3
# 2    3
# 3    3
# 4    3
# 5    3
# dtype: int64

# 第三类
# 元素函数应用

# 对某一列进行函数调用，Series用map
df['D'] = df['D'].map(lambda x : x ** 2)
print(df)
#     A   B   C    D
# 0   1   2   3   16
# 1   5   6   7   64
# 2   9  10  11  144
# 3  13  14  15  256
# 4  17  18  19  400
# 5  21  22  23  576

# 对整体
df = df.applymap(lambda x : np.sqrt(x))
# print(df)
#           A         B         C     D
# 0  1.000000  1.414214  1.732051   4.0
# 1  2.236068  2.449490  2.645751   8.0
# 2  3.000000  3.162278  3.316625  12.0
# 3  3.605551  3.741657  3.872983  16.0
# 4  4.123106  4.242641  4.358899  20.0
# 5  4.582576  4.690416  4.795832  24.0
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# API太多，请参考下面网站
# https://www.yiibai.com/pandas/python_pandas_working_with_text_data.html

# 本代码只罗列重要

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print(s)
# 0             tom
# 1    william rick
# 2            john
# 3         alber@t
# 4             NaN
# 5            1234
# 6      steveminsu
# dtype: object

# lower / upper
print(s.str.lower())

# len
print(s.str.len())
# 0     3.0
# 1    12.0
# 2     4.0
# 3     7.0
# 4     NaN
# 5     4.0
# 6    10.0
# dtype: float64

# strip，删除字符串两侧空格以及换行符
s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', ' 1 2 3 4     ', 'SteveMinsu'])
print(s)
# 0              Tom
# 1     William Rick
# 2             John
# 3          Alber@t
# 4     1 2 3 4
# 5       SteveMinsu
dtype: object

print(s.str.strip())

# 0             Tom
# 1    William Rick
# 2            John
# 3         Alber@t
# 4         1 2 3 4
# 5      SteveMinsu
# dtype: object

# spilt，分隔符
s = pd.Series(['1@2', 'sfdf@d@#@@'])
print(s.str.split('@'))
# 0              [1, 2]
# 1    [sfdf, d, #, , ]
# dtype: object

# cat连接符
s = pd.Series(list('ABCD'))
print(s.str.cat(sep = ' -> '))
# A -> B -> C -> D

# get_dummies()，返回one-hot形式
print(s.str.get_dummies())
#    A  B  C  D
# 0  1  0  0  0
# 1  0  1  0  0
# 2  0  0  1  0
# 3  0  0  0  1

# contains，返回布尔值
s = pd.Series(['1@2', 'sfdf@d@#@@'])
print(s.str.contains('@') & s.str.contains('d'))
# 0    False
# 1     True
# dtype: bool

# replace
print(s.str.replace('@#', 'q'))
# 0          1@2
# 1    sfdf@dq@@
# dtype: object

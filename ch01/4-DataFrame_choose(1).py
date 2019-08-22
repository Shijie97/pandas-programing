# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.permutation(28).reshape(7, 4), index = np.random.permutation(np.arange(1, 8)), columns = list('BCDA'))
print(df)
print('--' * 20)

# 单独选择'A'这一列，注意这种形式只能获取某一列，只能是一列
# 两种方式等价
print(df['A'])
print('--' * 20)
print(df.A)
print('--' * 20)
# 通过切片进行获取
print(df[2:6]) # 获取第2~5行
print('--' * 20)

print(df.loc[1])


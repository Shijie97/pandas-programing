# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# gruopby函数，根据某一列或者某几列将数据帧分组

df = pd.DataFrame({'Country':['China','China', 'India', 'India', 'America', 'Japan', 'China', 'India'],
                   'Income':[10000, 10000, 5000, 5002, 40000, 50000, 8000, 5000],
                    'Age':[5000, 4321, 1234, 4010, 250, 250, 4500, 4321]})
print(df)

#    Country  Income   Age
# 0    China   10000  5000
# 1    China   10000  4321
# 2    India    5000  1234
# 3    India    5002  4010
# 4  America   40000   250
# 5    Japan   50000   250
# 6    China    8000  4500
# 7    India    5000  4321

# 根据国家分组，返回的是个DataFrameGroupBy对象，该对象可以迭代
print(df.groupby('Country')) # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F536989888>

# 遍历该对象输出
for index, data in df.groupby('Country'):
    print(index)
    print(data)

# America
#    Country  Income  Age
# 4  America   40000  250
# China
#   Country  Income   Age
# 0   China   10000  5000
# 1   China   10000  4321
# 6   China    8000  4500
# India
#   Country  Income   Age
# 2   India    5000  1234
# 3   India    5002  4010
# 7   India    5000  4321
# Japan
#   Country  Income  Age
# 5   Japan   50000  250

# 根据国家和收入分组
for (index1, index2), data in df.groupby(['Country', 'Income']):
    print(index1, index2)
    print(data)

# America 40000
#    Country  Income  Age
# 4  America   40000  250
# China 8000
#   Country  Income   Age
# 6   China    8000  4500
# China 10000
#   Country  Income   Age
# 0   China   10000  5000
# 1   China   10000  4321
# India 5000
#   Country  Income   Age
# 2   India    5000  1234
# 7   India    5000  4321
# India 5002
#   Country  Income   Age
# 3   India    5002  4010
# Japan 50000
#   Country  Income  Age
# 5   Japan   50000  250

# 分组后进行，对每组进行聚合操作
# 对国家分组，对每组的剩余所有列求min，max，mean
print(df.groupby('Country').aggregate([np.max, np.min, np.mean]))
#         Income                        Age
#           amax   amin          mean  amax  amin         mean
# Country
# America  40000  40000  40000.000000   250   250   250.000000
# China    10000   8000   9333.333333  5000  4321  4607.000000
# India     5002   5000   5000.666667  4321  1234  3188.333333
# Japan    50000  50000  50000.000000   250   250   250.000000

# 根据国家进行分组后，仅对Age这一列求max和sum
print(df.groupby('Country').aggregate({'Age' : [np.max, np.sum]}))
#          amax    sum
# Country
# America   250    250
# China    5000  13821
# India    4321   9565
# Japan     250    250

# 获得某一个分组 get_group
print(df.groupby('Country').get_group('China'))
#   Country  Income   Age
# 0   China   10000  5000
# 1   China   10000  4321
# 6   China    8000  4500

# 如果要对分组后，每组的某一列进行操作
# 方法一，在[]中写入列名即可
print(df.groupby('Country')['Income'].aggregate(np.mean))
# Country
# America    40000.000000
# China       9333.333333
# India       5000.666667
# Japan      50000.000000
# Name: Income, dtype: float64

# 方法二，聚合函数中指定列名，指定对应的操作
print(df.groupby('Country').aggregate({'Income' : np.mean}))
#                Income
# Country
# America  40000.000000
# China     9333.333333
# India     5000.666667
# Japan    50000.000000

# 查看分组 .groups，返回字典，key为每个组的组名，value为值
print(df.groupby('Country').groups)
# {'America': Int64Index([4], dtype='int64'),
# 'China': Int64Index([0, 1, 6], dtype='int64'),
# 'India': Int64Index([2, 3, 7], dtype='int64'),
# 'Japan': Int64Index([5], dtype='int64')}

# 如果指向对分组后的某一组进行操作，可以先get_group，再聚合
# 求中国收入的平均值和总和
print(df.groupby('Country').get_group('China').aggregate({'Income' : [np.mean, np.sum]}))
#             Income
# mean   9333.333333
# sum   28000.000000

# 确定每个分组的大小，很显然，每列应该都是一模一样的，因为每组行数一样
print(df.groupby('Country').aggregate(np.size))
#          Income  Age
# Country
# America       1    1
# China         3    3
# India         3    3
# Japan         1    1
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np


# Series对象创建,
# 注意，数据是可以异构的
s = pd.Series([1, 3, 5, np.nan, 6, 'A'])
print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    A
# dtype: float64

print(type(s)) # <class 'pandas.core.series.Series'>

# data_range，从起始日期开始往后的十天
dates = pd.date_range('20190822', periods = 7)
print(dates)
# DatetimeIndex(['2019-08-22', '2019-08-23', '2019-08-24', '2019-08-25',
#                '2019-08-26', '2019-08-27', '2019-08-28', '2019-08-29',
#                '2019-08-30', '2019-08-31'],
#               dtype='datetime64[ns]', freq='D')

# 构造DataFrame对象，方法之一，传递numpy数组
# index为行索引，columns为列索引
df = pd.DataFrame(np.random.rand(7, 4), index = dates, columns = list('ABCD'))
print(df)
#                    A         B         C         D
# 2019-08-22  0.767074  0.218970  0.250417  0.306311
# 2019-08-23  0.466802  0.426528  0.370036  0.361371
# 2019-08-24  0.372805  0.298795  0.495114  0.070676
# 2019-08-25  0.817595  0.795797  0.704969  0.781827
# 2019-08-26  0.910036  0.723907  0.623871  0.095232
# 2019-08-27  0.732076  0.478744  0.047379  0.034906
# 2019-08-28  0.913025  0.552603  0.781210  0.141011

# 构造DataFrame对象，方法之二，传递字典
df2 = pd.DataFrame({
    'A' : 1.0, # A这一列都是常数1.0
    'B' : pd.Timestamp('20190822'), # 将字符串转化为时间戳的形式
    'C' : pd.Series(1, index = range(0, 4), dtype = 'float32'), # 传入一个Series，index相当于一位数组的下标
    'D' : np.array([3] * 4, dtype = 'int32'), # 传入一个np数组
    'E' : 'foo' # 字符串常量
})
print(df2)
#      A          B    C  D    E
# 0  1.0 2019-08-22  1.0  3  foo
# 1  1.0 2019-08-22  1.0  3  foo
# 2  1.0 2019-08-22  1.0  3  foo
# 3  1.0 2019-08-22  1.0  3  foo

# 查看dateFrame每一列的数据类型
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E            object
# dtype: object
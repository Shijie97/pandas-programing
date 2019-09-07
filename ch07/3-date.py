# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# pd.datetime.now()获取当前时间
print(pd.datetime.now()) # 2019-09-07 18:09:16.234664

# 创建一个时间戳
print(pd.Timestamp('20190907')) # 2019-09-07 00:00:00

# 创建一个时间范围
print(pd.date_range('12:00', '23:59', freq = '30min').time)
# [datetime.time(12, 0) datetime.time(12, 30) datetime.time(13, 0)
#  datetime.time(13, 30) datetime.time(14, 0) datetime.time(14, 30)
#  datetime.time(15, 0) datetime.time(15, 30) datetime.time(16, 0)
#  datetime.time(16, 30) datetime.time(17, 0) datetime.time(17, 30)
#  datetime.time(18, 0) datetime.time(18, 30) datetime.time(19, 0)
#  datetime.time(19, 30) datetime.time(20, 0) datetime.time(20, 30)
#  datetime.time(21, 0) datetime.time(21, 30) datetime.time(22, 0)
#  datetime.time(22, 30) datetime.time(23, 0) datetime.time(23, 30)]

# period表示总共几天
print(pd.date_range('20190907', periods = 5))
# DatetimeIndex(['2019-09-07', '2019-09-08', '2019-09-09', '2019-09-10',
#                '2019-09-11'],
#               dtype='datetime64[ns]', freq='D')

# 转化为时间戳，用to_datetime
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None])))
# 0   2009-07-31
# 1   2019-10-10
# 2          NaT
# dtype: datetime64[ns]
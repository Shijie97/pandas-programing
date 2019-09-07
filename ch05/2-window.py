# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# 与时间序列有关，窗口主要用于平滑数据

# rolling主要查看，每一天的最近n天的某种情况（比如平均值，求和啥的）
# rolling(self, window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None)
# window为整数时，表示观测值的数量
# min_periods默认为window的大小，表示最少包含观测值的个数
index=pd.date_range('20190116', periods = 7)
data=np.random.permutation(np.arange(1, 8))
s=pd.Series(data,index=index)
print(s)
# 2019-01-16    1
# 2019-01-17    6
# 2019-01-18    5
# 2019-01-19    7
# 2019-01-20    3
# 2019-01-21    4
# 2019-01-22    2
# Freq: D, dtype: int32

# 前两行为NaN是因为min_periods为3，最少包括的观测值为3，前两行都没有填满，直到第三行才填满，所以为NaN
print(s.rolling(3).mean())
# 2019-01-16         NaN
# 2019-01-17         NaN
# 2019-01-18    4.000000
# 2019-01-19    6.000000
# 2019-01-20    5.000000
# 2019-01-21    4.666667
# 2019-01-22    3.000000
# Freq: D, dtype: float64

# expanding表示，从头到每一天的变化情况
# expanding(self, min_periods=1, center=False, axis=0)
# min_periods=1表示最少观察的对象数
print(s.expanding(min_periods = 3).sum())
# 前两行为NaN是因为min_periods = 3，最少观测的数量为3
# 这里3可以这么理解，我要计算每行从头到该行的和，但是我希望从头到该行至少>=3天
# 2019-01-16     NaN
# 2019-01-17     NaN
# 2019-01-18    17.0
# 2019-01-19    22.0
# 2019-01-20    24.0
# 2019-01-21    27.0
# 2019-01-22    28.0
# Freq: D, dtype: float64
# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# filter操作仅仅是过滤出有用的行，类似于SQL中的where
# 与group结合的时候，是先分组，然后返回有用的组，这个时候，对应的组，要么全返回，要么全都不返回，即保证了组的完整性

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

print('-' * 100)
# 返回的满足条件的各个组，每个组行数都是完整的，每个组不会少行数，要么都有，要么都没有
# 传入函数的形参是整个数据帧，这些个数据帧包括每一列
# 返回的时候，所有列原样输出，分组的那一列不会提到最前面，也不会重复

# 查找分组后，质量小于等于32的那些组
print(df.groupby('order').filter(lambda x : np.max(x['quantity']) <= 32))
#     account       name  order       sku  quantity  unit price  ext price
# 0    383080   Will LLC  10001  B1-20000         7       33.69     235.83
# 1    383080   Will LLC  10001  S1-27722        11       21.12     232.32
# 2    383080   Will LLC  10001  B1-86481         3       35.99     107.97
# 8    218895  Kulas Inc  10006  S1-27722        32       95.66    3061.12
# 9    218895  Kulas Inc  10006  B1-33087        23       22.55     518.65
# 10   218895  Kulas Inc  10006  B1-33364         3       72.30     216.90
# 11   218895  Kulas Inc  10006  B1-20000        -1       72.18     -72.18
print('-' * 100)

# 查找分组后，account为383080的那些组
print(df.groupby('order').filter(lambda x : np.max(x['account']) == 383080))
#    account      name  order       sku  quantity  unit price  ext price
# 0   383080  Will LLC  10001  B1-20000         7       33.69     235.83
# 1   383080  Will LLC  10001  S1-27722        11       21.12     232.32
# 2   383080  Will LLC  10001  B1-86481         3       35.99     107.97
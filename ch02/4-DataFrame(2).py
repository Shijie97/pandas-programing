# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 从list的元素为字典的数据结构创建数据帧
# 感觉这种方式好麻烦，不如直接将data换成字典，k为col名，value为列表
# 这里每一个字典代表每一行，第一行因为没有c，所以为NaN
# 这种构造方式的好处之一就是方便认为给df添加一行
data = [{'a' : 1, 'b' : 2}, {'a' : 2, 'b' : 3, 'c' : 4}]
df = pd.DataFrame(data, index = [2, 3]) # 可以指定index内容
print(df)

#    a  b    c
# 2  1  2  NaN
# 3  2  3  4.0

# 如果强行指定col或者index呢？
# 结论：Pandas中，如果用字典构造系列和数据帧，如果强行指定index或者column，
# 则以强行指定的为准，指定的index或者column中没有，但是字典本身有的数据将被忽略，
# 指定的index或者column中有，但是字典本身没有的数据将被置NaN

# 指定的col中c没有，因此忽略
df1 = pd.DataFrame(data, columns = ['a', 'b'])
print(df1)

#    a  b
# 0  1  2
# 1  2  3

# 不仅c忽略，而且只有a和d，而d在字典中没有对应的值，所以为NaN
df2 = pd.DataFrame(data, columns = ['a', 'd'])
print(df2)

#    a   d
# 0  1 NaN
# 1  2 NaN

# 从系列创建数据帧
# 传递方式通过传一个字典，k为col名，v为系列
# 因为第一列没有四行，所以第四行为NaN
dic = {'col1' : pd.Series([1, 2, 3], index = [0, 1, 2]),
       'col2' : pd.Series([1, 2, 3, 4], index = [0, 1, 2, 3])}
df = pd.DataFrame(dic)
print(df)

#    col1  col2
# 0   1.0     1
# 1   2.0     2
# 2   3.0     3
# 3   NaN     4
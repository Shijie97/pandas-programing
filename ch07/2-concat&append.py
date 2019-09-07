# !user/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# concat用于将两个数据帧链接起来
# pd.concat([obj1, obj2])
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two])
print(rs)

#      Name subject_id  Marks_scored
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88

# 可以为每个部分标记一个关键字，注明keys即可
print(pd.concat([one, two], keys = ['x', 'y']))
#        Name subject_id  Marks_scored
# x 1    Alex       sub1            98
#   2     Amy       sub2            90
#   3   Allen       sub4            87
#   4   Alice       sub6            69
#   5  Ayoung       sub5            78
# y 1   Billy       sub2            89
#   2   Brian       sub4            80
#   3    Bran       sub3            79
#   4   Bryce       sub6            97
#   5   Betty       sub5            88

# 如果想统一index，需要置ignore_index为True
print(pd.concat([one, two], ignore_index = True))
#      Name subject_id  Marks_scored
# 0    Alex       sub1            98
# 1     Amy       sub2            90
# 2   Allen       sub4            87
# 3   Alice       sub6            69
# 4  Ayoung       sub5            78
# 5   Billy       sub2            89
# 6   Brian       sub4            80
# 7    Bran       sub3            79
# 8   Bryce       sub6            97
# 9   Betty       sub5            88

# 可以指定axis，如果为1则横向添加新列，列名可重复
print(pd.concat([one, two], axis = 1))
#      Name subject_id  Marks_scored   Name subject_id  Marks_scored
# 1    Alex       sub1            98  Billy       sub2            89
# 2     Amy       sub2            90  Brian       sub4            80
# 3   Allen       sub4            87   Bran       sub3            79
# 4   Alice       sub6            69  Bryce       sub6            97
# 5  Ayoung       sub5            78  Betty       sub5            88

# append也可以用来连接
print(one.append(two))
#      Name subject_id  Marks_scored
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88

# 可以连接多个对象
print(one.append([two] * 2))
#      Name subject_id  Marks_scored
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88
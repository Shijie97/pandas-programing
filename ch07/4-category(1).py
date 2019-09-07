# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 隐式地创建Categorical数据

players = ['Garsol', 'Hardon', 'Bill', 'Duran', 'James', 'Barter']
scores = [22, 34, 12, 31, 26, 19]
teams = ['West', 'West', 'East', 'West', 'East', 'East']
df = pd.DataFrame({'player': players, 'score': scores, 'team': teams})
print(df)
#    player  score  team
# 0  Garsol     22  West
# 1  Hardon     34  West
# 2    Bill     12  East
# 3   Duran     31  West
# 4   James     26  East
# 5  Barter     19  East

d=pd.Series(scores).describe()
print('-' * 20)
print(d)
# count     6.000000
# mean     24.000000
# std       8.074652
# min      12.000000
# 25%      19.750000
# 50%      24.000000
# 75%      29.750000
# max      34.000000
# dtype: float64

print('-' * 20)
print(df['team'])
# 0    West
# 1    West
# 2    East
# 3    West
# 4    East
# 5    East
# Name: team, dtype: object

# 静态添加
# 将team这一列转化为category
df['team'] = df['team'].astype('category')
print('-' * 20)
print(df['team'])
# 0    West
# 1    West
# 2    East
# 3    West
# 4    East
# 5    East
# Name: team, dtype: category
# Categories (2, object): [East, West]

# 动态添加
# 将高于平均分的划为 Star，低于平均分的划为 Role
score_ranges = [d['min']-1, d['mean'], d['max'] + 1] # 确定范围
score_labels = ['Role', 'Star'] # 标签值
df['level'] = pd.cut(df['score'], score_ranges, labels = score_labels)
print('-' * 20)
print(df['level'])
# 0    Role
# 1    Star
# 2    Role
# 3    Star
# 4    Star
# 5    Role
# Name: level, dtype: category
# Categories (2, object): [Role < Star]

print('-' * 20)
print(df['level'].array)
# [Role, Star, Role, Star, Star, Role]
# Categories (2, object): [Role < Star]
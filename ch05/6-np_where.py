# !user/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

a = np.arange(10)
print(a) # [0 1 2 3 4 5 6 7 8 9]

# where(condition, x, y)，condition是一个布尔变量，可以是array也可以是list，对应项为满足，则为x，否则为y
# 0为False，不满足，则为-1，其余为1
print(np.where(a, 1, -1)) # [-1  1  1  1  1  1  1  1  1  1]

# 如果只带condition，则只输出满足条件的值，形成一个元组，元组里面套着一个condition类型的对象，这里是数组
print(np.where(a > 5)) # (array([6, 7, 8, 9], dtype=int64),)
print(*np.where(a > 5)) # [6 7 8 9]

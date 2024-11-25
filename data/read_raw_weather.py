import math
from itertools import groupby

import numpy as np

from utils import read_xls, write_xls


def sigma(l: list[float]):
    s = 0
    for i in l:
        if not math.isnan(i):
            s += i
    return s


def mean(l: list[float]):
    return sigma(l) / len(l)


PATH = '青岛市天气.xls'

# ################### 读取原始数据 ####################

data = read_xls('./raw/' + PATH)[:, 1:]
data = {key: tuple(group) for key, group in groupby(data, key=lambda x: (x[0], x[1]))}

print(data)

# ################### 处理数据 ###############

res = {}
for ym in data:
    res[ym] = [
        ym[0],
        ym[1],
        mean([row[2] for row in data[ym]]),
        mean([row[3] for row in data[ym]]),
        mean([row[4] for row in data[ym]]),
        mean([row[5] for row in data[ym]]),
        sigma([row[6] for row in data[ym]])
    ]

print(res)

# 保存为xlsx文件
write_xls('./processed/' + PATH + 'x', np.array(list(res.values())))

# import statistics as stat

import numpy as np
from matplotlib import pyplot as plt

from utils import read_xls

CITY = '重庆市'
PATH = f'./processed/{CITY}.xlsx'

data = read_xls(PATH)[73:]
X = np.arange(1, len(data) + 1)
Y = data[:, 3]

print(X, Y)

plt.title('PM2.5 - t graph')
plt.xlabel('t / month')
plt.ylabel('PM2.5 / (μg/m³)')
# plt.xlim(xlim)
# plt.ylim(ylim)
plt.xticks(ticks=[0, 12, 24, 36, 48, 60])
plt.grid()
plt.plot(X, Y)

plt.savefig(f'./{CITY}_PM25_t.png')
plt.show()

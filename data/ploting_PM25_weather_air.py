import statistics as stat

import numpy as np
from matplotlib import pyplot as plt

from utils import read_xls

CITY = b'\xe6\xb5\x8e\xe5\x8d\x97\xe5\xb8\x82'.decode()
PATH = f'./processed/{CITY}.xlsx'

data = read_xls(PATH)[73:]


# print(data)

def draw_scatter(title: str, varX: str, varY: str, X: np.array, Y: np.array, xlim=None, ylim=None):
    print(X[0], Y[0])
    print(r := stat.correlation(X, Y))

    plt.title(f'{title}    (r = {r:.3f})')
    plt.xlabel(varX)
    plt.ylabel(varY)
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    plt.grid()

    plt.scatter(X, Y)

    # plt.savefig(f'./graph/{CITY} {title}.png')
    plt.show()


# T
draw_scatter('PM2.5 - T graph', 'T / °C', 'PM2.5 / (μg/m³)', data[:, 9], data[:, 3])
# P
draw_scatter('PM2.5 - P graph', 'P / mmHg', 'PM2.5 / (μg/m³)', data[:, 10], data[:, 3])
# U
draw_scatter('PM2.5 - U graph', 'U / %', 'PM2.5 / (μg/m³)', data[:, 11], data[:, 3])
# Ff
draw_scatter('PM2.5 - Ff graph', 'Ff / (m/s)', 'PM2.5 / (μg/m³)', data[:, 12], data[:, 3])
# RRR
draw_scatter('PM2.5 - RRR graph', 'RRR / mm', 'PM2.5 / (μg/m³)', data[:, 13], data[:, 3])

# PM10
draw_scatter('PM2.5 - PM10 graph', 'PM10 / (μg/m³)', 'PM2.5 / (μg/m³)', data[:, 4], data[:, 3])
# CO
draw_scatter('PM2.5 - CO graph', 'CO / (mg/m³)', 'PM2.5 / (μg/m³)', data[:, 5], data[:, 3])
# NO2
draw_scatter('PM2.5 - NO2 graph', 'NO2 / (μg/m³)', 'PM2.5 / (μg/m³)', data[:, 6], data[:, 3])
# SO2
draw_scatter('PM2.5 - SO2 graph', 'SO2 / (μg/m³)', 'PM2.5 / (μg/m³)', data[:, 7], data[:, 3])
# O3
draw_scatter('PM2.5 - O3 graph', 'O3 / (μg/m³)', 'PM2.5 / (μg/m³)', data[:, 8], data[:, 3])

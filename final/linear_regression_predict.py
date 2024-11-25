import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt

from utils import read_xls

read = read_xls('./processed/济南市.xlsx')

CO = read[:, 5]
O3 = read[:, 8]
T = read[:, 9]
P = read[:, 10]
t = np.arange(1, len(CO) + 1)
sint = np.sin(6 / np.pi * t)
PM25 = read[:, 3]

data_part = {
    'CO': list(CO[:-12]),
    'O3': list(O3[:-12]),
    'T': list(T[:-12]),
    'P': list(P[:-12]),
    't': list(t[:-12]),
    'sint': list(sint[:-12]),

    'PM25': list(PM25[:-12])
}
data = {
    'CO': list(CO),
    'O3': list(O3),
    'T': list(T),
    'P': list(P),
    't': list(t),
    'sint': list(sint),

    'PM25': list(PM25)
}

# 创建DataFrame
df_part = pd.DataFrame(data_part)
df = pd.DataFrame(data)

# 定义自变量和因变量
X = df[['CO', 'O3', 'T', 'P', 't', 'sint']]  # 自变量
X_part = df_part[['CO', 'O3', 'T', 'P', 't', 'sint']]  # 自变量
y = df['PM25']  # 因变量
y_part = df_part['PM25']  # 因变量

# 添加常数项，以计算截距
X = sm.add_constant(X)
X_part = sm.add_constant(X_part)

# 创建并拟合模型
model = sm.OLS(y_part, X_part).fit()

# 输出模型的摘要
print(model.summary())

# 预测
y_pred = model.predict(X)

plt.xlabel('t / month')
plt.ylabel('PM2.5 / (μg/m³)')

plt.plot(t[:12], y[-12:], color='blue')
plt.plot(t[:12], y_pred[-12:], color='red')

plt.savefig('./predict.png')
plt.show()

t = t[-12:]
y = y[-12:]
y_pred = y_pred[-12:]
y_bar = np.mean(y)
R = ((y_pred - y_bar)**2).sum() / ((y - y_bar)**2).sum()
print(R)

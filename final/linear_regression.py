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
df = pd.DataFrame(data)

# 定义自变量和因变量
X = df[['CO', 'O3', 'T', 'P', 't', 'sint']]  # 自变量
y = df['PM25']  # 因变量

# 添加常数项，以计算截距
X = sm.add_constant(X)

# 创建并拟合模型
model = sm.OLS(y, X).fit()

# 输出模型的摘要
print(model.summary())

# 预测
y_pred = model.predict(X)

plt.plot(t, y)
plt.plot(t, y_pred, color='red')

plt.show()

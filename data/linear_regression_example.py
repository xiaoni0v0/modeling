import pandas as pd
import statsmodels.api as sm

# 创建示例数据
data = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [2, 3, 4, 5, 6],
    'Y': [5, 7, 9, 11, 13]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 定义自变量和因变量
X = df[['X1', 'X2']]  # 自变量
y = df['Y']  # 因变量

# 添加常数项，以计算截距
X = sm.add_constant(X)

# 创建并拟合模型
model = sm.OLS(y, X).fit()

# 输出模型的摘要
print(model.summary())

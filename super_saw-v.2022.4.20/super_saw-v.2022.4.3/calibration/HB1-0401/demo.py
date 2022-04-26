import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# df = pd.read_csv("./0401.csv", names=["temp", "f1", "f2", "f3", "f4", "f5"])
# 数据在降温过程中测得
df = pd.DataFrame({
    "f1": [429151122, 429075774, 429003675, 428924588, 428845209],
    "temp": [61.27, 56.27, 51.27, 46.23, 41.27]
})


x = df["f1"].values.reshape((-1, 1))
y = df["temp"].values

transformer = PolynomialFeatures(degree=2, include_bias=False)
x_new = transformer.fit_transform(x)

model = LinearRegression().fit(x_new, y)
r_sq = model.score(x_new, y)
print(f'coefficient of determination (R^2): {r_sq:.2f}')
print(f"intercept: {model.intercept_:.3f}")
print(f"slope: {model.coef_}")

y_pred = model.predict(x_new)

# x2 is used for fitting curve plot
# x2 = np.linspace(x[0], x[-1], 1601).reshape((-1, 1))

# extend the prediction range to see the fitting quality
x2 = np.linspace(x[0] - (x[-1] - x[0]), x[-1] + (x[-1] - x[0]), 1601).reshape((-1, 1))
x2_new = transformer.fit_transform(x2)
y2_pred = model.predict(x2_new)

# y_equation_validation = model.intercept_ + model.coef_[0]*x2 + model.coef_[1]*x2**2
# # number of points for 1 Hz resolution
# num_1Hz = int((len(x) - 1)*1e4 + 1)
# print(f"length of x is {len(x)}")
# print(f"length of x (1 Hz) is {num_1Hz}")
# x2 = np.linspace(x[0], x[-1], num_1Hz).reshape((-1, 1))  # improve the resolution from 10 kHz to 1 Hz
# x2_new = transformer.fit_transform(x2)
# y2_pred = model.predict(x_new)

# temp = x2[np.argmax(y2_pred)][0]
# print(f"temp is {freq*1e6:,.0f}")
print(f"fitting score is {r_sq:.3f}")

# # print(df)
fig, ax = plt.subplots()
ax.scatter(x, y, color="blue", label="measured")
ax.scatter(x, y_pred, color="red", marker="s")
ax.plot(x2, y2_pred, color="red", label="fitted")
# ax.plot(x2, y_equation_validation, color="green", label="equation validation") 
# ax.scatter([1, 2, 3], [1, 2, 3])
ax.legend()
plt.show()
# print(df.head)


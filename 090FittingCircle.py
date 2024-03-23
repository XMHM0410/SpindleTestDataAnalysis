import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from utils import plotThree,plotOne
from NoiseReduction import wavelet,kalman,average
# %%导入偏心误差数据
pdi1 = pd.read_csv('Data\SyncAndAsyncData.csv')
r = pdi1["Pos"].values
theta = pdi1["theta"].values
# %%转换为直角坐标系
x = r * np.cos(theta)
y = r * np.sin(theta)
# %%定义最小二乘圆方程
def circle_equation(params):
    x0, y0, r = params
    return (x - x0)**2 + (y - y0)**2 - r**2
# %%初始参数猜测
initial_guess = [0, 0, 1]
# %%最小二乘优化
result = least_squares(circle_equation, initial_guess)
# %%输出结果
print("圆心坐标 (x0, y0):", result.x[:2])
theta_circle = np.arctan2(result.x[1], result.x[0])
print("圆心坐标 (r, theta):", np.sqrt(result.x[0]**2 + result.x[1]**2), theta_circle)
print("半径 r:", result.x[2])
# %%绘制原始点
plt.scatter(x, y, label='Original points')
# %%计算拟合圆上的点
num_points = 100
theta_fit = np.linspace(0, 2*np.pi, num_points)
x_fit = result.x[0] + result.x[2] * np.cos(theta_fit)
y_fit = result.x[1] + result.x[2] * np.sin(theta_fit)
# %%绘制拟合圆
plt.plot(x_fit, y_fit, label='Fitted circle')
# 设置图例
plt.legend()
# 设置标题和坐标轴标签
plt.title('Least Squares Circle Fitting')
plt.xlabel('x')
plt.ylabel('y')
# 显示图像
plt.show()
# 圆心坐标 (x0, y0): [-2.87020791e-05  1.44384104e-05]
# 圆心坐标 (r, theta): 3.212906848800992e-05 2.675512763170522
# 半径 r: 0.35403725020010507
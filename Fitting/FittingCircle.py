import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
# %%计算最小二乘结果
def least_square_cal(theta,pos,r = 12.8):
    # %%添加半径
    r = pos*0.001 + r
    # %%转换为直角坐标系
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # %%定义最小二乘圆方程
    def circle_equation(params):
        x0, y0, r = params
        return (x - x0)**2 + (y - y0)**2 - r**2
    # %%最小二乘优化
    initial_guess = [0, 0, 0]# 初始参数猜测
    result = least_squares(circle_equation, initial_guess) # 最小二乘优化
    # 计算圆心坐标和半径输出结果
    output = {}
    output["cartesian_coordinate"] = result.x[:2] # 圆心坐标 (x0, y0)
    theta_circle = np.arctan2(result.x[1], result.x[0])
    output["polar_coordinate"] = np.sqrt(result.x[0]**2 + result.x[1]**2), theta_circle # 圆心坐标 (r, theta)
    output["r"] = result.x[2] # 半径 r
    return output
# %%计算拟合圆上的点
# num_points = 100
# theta_fit = np.linspace(0, 2*np.pi, num_points)
# x_fit = result.x[0] + result.x[2] * np.cos(theta_fit)
# y_fit = result.x[1] + result.x[2] * np.sin(theta_fit)
# %%绘图
# plt.scatter(x, y, label='Original points') # 绘制原始点
# plt.plot(x_fit, y_fit, label='Fitted circle') # 绘制拟合圆
# plt.legend() # 设置图例
# plt.title('Least Squares Circle Fitting') # 设置标题和坐标轴标签
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
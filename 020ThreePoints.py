import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from utils import plotThree,plotOne
# %% 测量原始数据
df = pd.read_csv('Data\OriginalSignal.csv')
s1 = df["s1"].values
s2 = df["s2"].values
s3 = df["s3"].values
# %% 读取基本参数
# %%读文件基本参数
dfi2 = pd.read_csv('Data\config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
alpha = dfi2["alpha"].values[0]
beta = dfi2["beta"].values[0]
# 权系数c1 c2 c3
c1 = 1
c2 = -np.sin(np.deg2rad(alpha+beta))/np.sin(np.deg2rad(beta))
c3 = np.sin(np.deg2rad(alpha))/np.sin(np.deg2rad(beta))
print("c1:",c1,"c2:",c2,"c3:",c3)
# 生成时间和角度轴信息
N = len(s1) # 采样总点数
t_total = N/fs # 采样总时长
deg = 360*((rpm/60)*t_total)# 该段时间内转过的角度
t = np.arange(0,t_total,t_total/N) #生成时间轴
theta = np.arange(0,deg,deg/N) #生成角度轴 取10圈的数据
# %%三点法计算
S = s1*c1+s2*c2+s3*c3 # 三点法表达式
plotOne.plotOne(theta,S)
plt.show()
# %%文件保存
df1 = pd.DataFrame({"t":t,"theta":theta,"S":S,'s1':s1,'s2':s2,'s3':s3})
df1.to_csv('Data\MixedSignal.csv')
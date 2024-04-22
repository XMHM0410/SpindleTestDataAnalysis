import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import plotThree,plotOne
from NoiseReduction import wavelet,kalman,average
from Fitting import FittingCircle,MaxMinAvgCal
# %%导入误差数据
addr = 'Data\\Fanuc6000-90\\'
# 传统频域方法的
pdi1 = pd.read_csv(addr+'avg\\'+'01circle1_sync.csv')
theta1 = pdi1["theta"].values
sync1 = pdi1["AvgCircle"].values # 传统分离方法同步误差单圈集合平均数据
pdi2 = pd.read_csv(addr+'avg\\'+'02circle1_async.csv')
async1 = pdi2["AvgCircle"].values # 传统分离方法异步误差单圈集合平均数据
pdi3 = pd.read_csv(addr+'avg\\'+'03circle1_rod.csv')
rod1 = pdi3["AvgCircle"].values # 传统分离方法圆度误差单圈集合平均数据
pdi4 = pd.read_csv(addr+'avg\\'+'04circle1_pos.csv')
pos1 = pdi4["AvgCircle"].values # 传统分离方法偏心误差单圈集合平均数据
# 改进分离方法的
pdi5 = pd.read_csv(addr+'avg\\'+'05circle2_sync.csv')
theta2 = pdi5["theta"].values
sync2 = pdi5["AvgCircle"].values # 改进分离方法同步误差单圈集合平均数据
pdi6 = pd.read_csv(addr+'avg\\'+'06circle2_async.csv')
async2 = pdi6["AvgCircle"].values # 改进分离方法异步误差单圈集合平均数据
pdi7 = pd.read_csv(addr+'avg\\'+'07circle2_rod.csv')
rod2 = pdi7["AvgCircle"].values # 改进分离方法圆度误差单圈集合平均数据
pdi8 = pd.read_csv(addr+'avg\\'+'08circle2_pos.csv')
pos2 = pdi8["AvgCircle"].values # 改进分离方法偏心误差单圈集合平均数据
# %% 计算同步异步误差的最大最小平均值
# 传统频域方法的
sync1_cal = MaxMinAvgCal.calculate_stats(sync1)
async1_cal = MaxMinAvgCal.calculate_stats(async1)
rod1_cal = MaxMinAvgCal.calculate_stats(rod1)
pos1_cal = MaxMinAvgCal.calculate_stats(pos1)
# 改进分离方法的
sync2_cal = MaxMinAvgCal.calculate_stats(sync2)
async2_cal = MaxMinAvgCal.calculate_stats(async2)
rod2_cal = MaxMinAvgCal.calculate_stats(rod2)
pos2_cal = MaxMinAvgCal.calculate_stats(pos2)
# %% 计算最小二乘圆
# 传统频域方法的
sync1_fit = FittingCircle.least_square_cal(theta1,sync1)
async1_fit = FittingCircle.least_square_cal(theta1,async1)
rod1_fit = FittingCircle.least_square_cal(theta1,rod1)
pos1_fit = FittingCircle.least_square_cal(theta1,pos1)
# 改进分离方法的
sync2_fit = FittingCircle.least_square_cal(theta2,sync2)
async2_fit = FittingCircle.least_square_cal(theta2,async2)
rod2_fit = FittingCircle.least_square_cal(theta2,rod2)
pos2_fit = FittingCircle.least_square_cal(theta2,pos2)
# %%导出字符串
# 传统频域方法的
string_to_export =  "sync1_cal" + str(sync1_cal)  +"\n"
string_to_export += "async1_cal"+ str(async1_cal) +"\n"
string_to_export += "rod1_cal"+ str(rod1_cal) +"\n"
string_to_export += "pos1_cal"+ str(pos1_cal) +"\n"
string_to_export += "sync1_fit"+ str(sync1_fit) +"\n"
string_to_export += "async1_fit"+ str(async1_fit) +"\n"
string_to_export += "rod1_fit"+ str(rod1_fit) +"\n"
string_to_export += "pos1_fit"+ str(pos1_fit) +"\n"
# 改进分离方法的
string_to_export += "sync2_cal"+ str(sync2_cal) +"\n"
string_to_export += "async2_cal"+ str(async2_cal) +"\n"
string_to_export += "rod2_cal"+ str(rod2_cal) +"\n"
string_to_export += "pos2_cal"+ str(pos2_cal) +"\n"
string_to_export += "sync2_fit"+ str(sync2_fit) +"\n"
string_to_export += "async2_fit"+ str(async2_fit) +"\n"
string_to_export += "rod2_fit"+ str(rod2_fit) +"\n"
string_to_export += "pos2_fit"+ str(pos2_fit) +"\n"
# 输出
print(string_to_export)
with open(addr+"13FittingCircle.txt", "w", encoding="utf-8") as file: # 使用 open 函数打开（或创建）一个文件，并选择写入模式 'w'
    file.write(string_to_export)# 将字符串写入到文件中
out2 = pd.DataFrame({'theta':theta1,'sync1':sync1,'async1':async1,'rod1':rod1,'pos1':pos1,'sync2':sync2,'async2':async2,'rod2':rod2,'pos2':pos2})
out2.to_csv(addr+"14ResultCircle.csv",index=False)
# 图用60x40
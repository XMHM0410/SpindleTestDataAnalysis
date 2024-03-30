import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%读文件三点法混合信号
# %%导入偏心误差数据
addr = 'Data\\Fanuc6000-90\\'
pdi1 = pd.read_csv(addr+'05SyncAndAsyncData.csv')
sync1 = pdi1["Sync"].values
async1 = pdi1["Async"].values
rod1 = pdi1["Rod"].values
pos1 = pdi1["Pos"].values
theta1 = pdi1["theta"].values
pdi2 = pd.read_csv(addr+'11SyncAndAsync2Data.csv')
sync2 = pdi2["Sync"].values
async2 = pdi2["Async"].values
rod2 = pdi2["Rod"].values
pos2 = pdi2["Pos"].values
theta2 = pdi2["theta"].values
# %%获取基本参数
dfi2 = pd.read_csv(addr+'00config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
def config(S):
    N = len(S) # 总点数
    t_total = N/fs # 总时长
    loop = int((rpm/60)*t_total)# 转过的圈数
    colom = int(N/loop)
    print(loop,colom)
    return loop,colom
# %%把S均分成loop段,形成单圈数据,并计算集合平均圈
def split(S,loop,colom):
    S_loop = {}
    S_loop_m = np.zeros((loop,colom))
    for i in range(loop):
        loop_name = "loop"+str(i+1)
        S_loop_m[i,:] = S[i*colom:(i+1)*colom]
        S_loop[loop_name] = S[i*colom:(i+1)*colom]
    S_loop["AvgCircle"] = np.mean(S_loop_m, axis=0)
    return S_loop
# %%传统分离方法同步误差单圈数据拆分+集合平均数据输出
loop1_sync,colom1_sync = config(sync1)
circle1_sync = split(sync1,loop1_sync,colom1_sync)
circle1_sync["theta"] = theta1[0:colom1_sync]
dfo1_sync = pd.DataFrame(circle1_sync)
dfo1_sync.to_csv(addr+'avg\\'+'01circle1_sync.csv', index=False)
print("传统分离方法同步误差单圈数据拆分+集合平均数据输出完成")
# %%传统分离方法异步误差单圈数据拆分+集合平均数据输出
loop1_async,colom1_async = config(async1)
circle1_async = split(async1,loop1_async,colom1_async)
circle1_async["theta"] = theta1[0:colom1_async]
dfo1_async = pd.DataFrame(circle1_async)
dfo1_async.to_csv(addr+'avg\\'+'02circle1_async.csv', index=False)
print("传统分离方法异步误差单圈数据拆分+集合平均数据输出完成")
# %%传统分离方法圆度误差单圈数据拆分+集合平均数据输出
loop1_rod,colom1_rod = config(rod1)
circle1_rod = split(rod1,loop1_rod,colom1_rod)
circle1_rod["theta"] = theta1[0:colom1_rod]
dfo1_rod = pd.DataFrame(circle1_rod)
dfo1_rod.to_csv(addr+'avg\\'+'03circle1_rod.csv', index=False)
print("传统分离方法圆度误差单圈数据拆分+集合平均数据输出完成")
# %%传统分离方法偏心误差单圈数据拆分+集合平均数据输出
loop1_pos,colom1_pos = config(pos1)
circle1_pos = split(pos1,loop1_pos,colom1_pos)
circle1_pos["theta"] = theta1[0:colom1_pos]
dfo1_pos = pd.DataFrame(circle1_pos)
dfo1_pos.to_csv(addr+'avg\\'+'04circle1_pos.csv', index=False)
print("传统分离方法偏心误差单圈数据拆分+集合平均数据输出完成")
# %%传统分离方法完成
print("传统分离方法完成")
# %%改进分离方法同步误差单圈数据拆分+集合平均数据输出
loop2_sync,colom2_sync = config(sync2)
circle2_sync = split(sync2,loop2_sync,colom2_sync)
circle2_sync["theta"] = theta2[0:colom2_sync]
dfo2_sync = pd.DataFrame(circle2_sync)
dfo2_sync.to_csv(addr+'avg\\'+'05circle2_sync.csv', index=False)
print("改进分离方法同步误差单圈数据拆分+集合平均数据输出完成")
# %%改进分离方法异步误差单圈数据拆分+集合平均数据输出
loop2_async,colom2_async = config(async2)
circle2_async = split(async2,loop2_async,colom2_async)
circle2_async["theta"] = theta2[0:colom2_async]
dfo2_async = pd.DataFrame(circle2_async)
dfo2_async.to_csv(addr+'avg\\'+'06circle2_async.csv', index=False)
print("改进分离方法异步误差单圈数据拆分+集合平均数据输出完成")
# %%改进分离方法圆度误差单圈数据拆分+集合平均数据输出
loop2_rod,colom2_rod = config(rod2)
circle2_rod = split(rod2,loop2_rod,colom2_rod)
circle2_rod["theta"] = theta2[0:colom2_rod]
dfo2_rod = pd.DataFrame(circle2_rod)
dfo2_rod.to_csv(addr+'avg\\'+'07circle2_rod.csv', index=False)
print("改进分离方法圆度误差单圈数据拆分+集合平均数据输出完成")
# %%改进分离方法偏心误差单圈数据拆分+集合平均数据输出
loop2_pos,colom2_pos = config(pos2)
circle2_pos = split(pos2,loop2_pos,colom2_pos)
circle2_pos["theta"] = theta2[0:colom2_pos]
dfo2_pos = pd.DataFrame(circle2_pos)
dfo2_pos.to_csv(addr+'avg\\'+'08circle2_pos.csv', index=False)
print("改进分离方法偏心误差单圈数据拆分+集合平均数据输出完成")
# %%传统分离方法完成
print("改进分离方法完成")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %% 读文件
addr = addr = 'Data\\Fanuc1000-90\\'
df = pd.read_csv(addr+'03MixedSignal.csv')
S = df["S"].values
t = df["t"].values
theta = df["theta"].values
# %%计算imf分量的重构
dfi1 = pd.read_csv(addr+'07Circles.csv')
loops = {}
for i in range(dfi1.shape[1]): # 循环所有圈
    loop= dfi1[f"loop{i+1}"].values # 获得当前单圈数据
    dfi2 = pd.read_csv(addr+"IMFs\\"+f'loop{i+1}NR.csv') # 获取当前单圈的IMF数据
    imf_NR = []
    for j in range(dfi2.shape[1]-1): # 获取每个IMF分量 减1为了把res去掉
        imfNR = dfi2[f"IMFNR{j+1}"].values #当前单个IMF分量
        imf_NR.append(imfNR) # 计入合并数组
    S_rebuild = np.sum(imf_NR, axis=0)
    loops[f"loop{i+1}_rebuild"] = S_rebuild
    print(f"loop{i+1} rebuild over")
out = pd.DataFrame(loops)
out.to_csv(addr+f'08RebuildCircles.csv', index=False)
# %% loops中所有键的值收尾相接生成重构信号
Rebuild_S = []
for i in range(len(loops)):
    Rebuild_S.append(loops[f"loop{i+1}_rebuild"])
Rebuild_S = np.concatenate(Rebuild_S, axis=0)
out2 = pd.DataFrame({"t":t[0:len(Rebuild_S)],"theta":theta[0:len(Rebuild_S)],"Rebuild_S":Rebuild_S})
out2.to_csv(addr+f'09RebuildSignal.csv', index=False)
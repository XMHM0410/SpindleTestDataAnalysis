import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%读文件三点法混合信号
df = pd.read_csv('Data\MixedSignal.csv')
S = df["S"].values
t = df["t"].values
theta = df["theta"].values
# %%读文件基本参数
dfi2 = pd.read_csv('Data\config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
N = len(S) # 采样点数
t_total = N/fs # 采样总时长
loop = int((rpm/60)*t_total)# 转过的圈数
colom = int(N/loop)
print(loop,colom)
# %%把S均分成loop段
S_loop = np.zeros((loop,colom))
for i in range(loop):
    S_loop[i,:] = S[i*colom:(i+1)*colom]
print(S_loop)
# %% 取S_loop的每一列数，计算其平均值，形成OneCircle数组
OneCircle_means = np.mean(S_loop, axis=0)
# %% 保存到文件
dfo1 = pd.DataFrame({'t':t[0:colom],# 截取一圈长度的t
                     'theta':theta[0:colom],
                     'OneCircle':OneCircle_means})
dfo1.to_csv('Data\OneCircle.csv',index=False)
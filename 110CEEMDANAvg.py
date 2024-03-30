import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CEEMDAN import ceemdan
import time
# %%读文件三点法混合信号
addr = 'Data\\Fanuc6000-90\\'
dfi1 = pd.read_csv(addr+'03MixedSignal.csv')
S = dfi1["S"].values
t = dfi1["t"].values
theta = dfi1["theta"].values
dfi2 = pd.read_csv(addr+'07Circles.csv')
loops = {}
# %%获取基本参数
dfi2 = pd.read_csv(addr+'00config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
N = len(S) # 总点数
t_total = N/fs # 总时长
loop = int((rpm/60)*t_total)# 转过的圈数
colom = int(N/loop)
# %%平均单圈信号保存
tt = time.time()
S_loop_m = np.zeros((loop,colom))
for i in range(loop):
    loop_name = "loop"+str(i+1)
    S_loop_m[i,:] = S[i*colom:(i+1)*colom]
AvgCircle = np.mean(S_loop_m, axis=0)
output = {"AvgCircle":AvgCircle,"theta":theta[0:len(AvgCircle)]}
df2 = pd.DataFrame(output)
df2.to_csv(addr+"avg-one\\"+"01AvgCircle.csv", index=False)
print('AvgCircle Done, Time used: {} sec'.format(time.time()-tt))
# %%平均圈信号CEEMDAN分解
tt = time.time()
elec_all_day_test = AvgCircle.copy()
IImfs,res=ceemdan.ceemdan_decompose(np.array(elec_all_day_test).ravel())
output = {"res":res}
for k in range(IImfs.shape[0]):
    output[f"IMF{k+1}"] = IImfs[k]
df2 = pd.DataFrame(output)
df2.to_csv(addr+"avg-one\\"+"02AvgIMFs.csv", index=False)
print('CEEMDAN Done, Time used: {} sec'.format(time.time()-tt))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CEEMDAN import ceemdan
import time
# %%读文件三点法混合信号
addr = 'Data\\Fanuc12000-90\\'
dfi1 = pd.read_csv(addr+'03MixedSignal.csv')
# S = dfi1["S"].values
t = dfi1["t"].values
theta = dfi1["theta"].values
dfi2 = pd.read_csv(addr+'07Circles.csv')
loops = {}
for i in range(dfi2.shape[1]):
    loops[f"loop{i+1}"] = dfi2[f"loop{i+1}"].values
    print(f"loop{i+1} read done")
# OneCircle_means = np.mean(S_loop, axis=0)
# %%CEEMDAN分解
for j in range(len(loops)):
    tt = time.time()
    elec_all_day_test = loops[f"loop{j+1}"].copy()
    IImfs,res=ceemdan.ceemdan_decompose(np.array(elec_all_day_test).ravel())
    # # IMF为IMF分量矩阵，res为分解残余量，也叫重建误差
    output = {"res":res}
    for k in range(IImfs.shape[0]):
        output[f"IMF{k+1}"] = IImfs[k]
    # %%文件保存
    df1 = pd.DataFrame(output)
    df1.to_csv(addr+"IMFs\\"+f"loop{j+1}.csv", index=False)
    print(f"loop{j+1} ceemdan done")
    print('Time used: {} sec'.format(time.time()-tt))
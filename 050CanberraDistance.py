import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CanberraDistance import canberraDistance
# %%计算imf分量的改进兰氏距离
addr = addr = 'Data\\Fanuc6000-90\\'
dfi1 = pd.read_csv(addr+'07Circles.csv')
for i in range(dfi1.shape[1]): # 循环所有圈
    loop= dfi1[f"loop{i+1}"].values # 获得当前单圈数据
    dfi2 = pd.read_csv(addr+"IMFs\\"+f'loop{i+1}.csv') # 获取当前单圈的IMF数据
    cd = {}
    for j in range(dfi2.shape[1]-1): # 获取每个IMF分量 减1为了把res去掉
        imf = dfi2[f"IMF{j+1}"].values #当前单个IMF分量
        cd[f"IMFcd{j+1}"] = canberraDistance.canberry_distance(imf, loop)
        print(f"IMF{j+1} cd over")
    print(f"loop{i+1} cd over")
    out = pd.DataFrame(cd)
    out.to_csv(addr+"IMFs\\"+f'loop{i+1}cd.csv', index=False)
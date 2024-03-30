import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CanberraDistance import canberraDistance
# 获取平均圈
addr = addr = 'Data\\Fanuc6000-90\\'
dfi0 = pd.read_csv(addr+"avg-one\\"+"01AvgCircle.csv")
loop= dfi0["AvgCircle"].values # 获得当前单圈数据
# %%计算imf分量的改进兰氏距离
dfi1 = pd.read_csv(addr+"avg-one\\"+"02AvgIMFs.csv")
cd = {}
for j in range(dfi1.shape[1]-1): # 获取每个IMF分量 减1为了把res去掉
    imf = dfi1[f"IMF{j+1}"].values #当前单个IMF分量
    cd[f"IMFcd{j+1}"] = canberraDistance.canberry_distance(imf, loop)
    print(f"IMF{j+1} cd over")
out = pd.DataFrame(cd)
out.to_csv(addr+"avg-one\\"+"03AvgIMFsCD.csv", index=False)
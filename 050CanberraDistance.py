import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CanberraDistance import canberraDistance
# %%读文件中的imf1-10
dfi1 = pd.read_csv('Data\OneCircle.csv')
S = dfi1["OneCircle"].values
theta = dfi1["theta"].values
dfi2 = pd.read_csv('Data\IMFs.csv')
imf1 = dfi2["IMF1"].values
imf2 = dfi2["IMF2"].values
imf3 = dfi2["IMF3"].values
imf4 = dfi2["IMF4"].values
imf5 = dfi2["IMF5"].values
# imf6 = dfi2["IMF6"].values
# imf7 = dfi2["IMF7"].values
# %%计算imf1-11的兰氏距离
cd1 = canberraDistance.canberry_distance(imf1, S)
print("cd1 over")
cd2 = canberraDistance.canberry_distance(imf2, S)
print("cd2 over")
cd3 = canberraDistance.canberry_distance(imf3, S)
print("cd3 over")
cd4 = canberraDistance.canberry_distance(imf4, S)
print("cd4 over")
cd5 = canberraDistance.canberry_distance(imf5, S)
print("cd5 over")
# cd6 = canberraDistance.canberry_distance(imf6, S)
print("cd6 over")
# cd7 = canberraDistance.canberry_distance(imf7, S)
# print("cd71 over")
# %%输出文件
out = pd.DataFrame({'cd1': cd1,
                    'cd2': cd2, 
                    'cd3': cd3, 
                    'cd4': cd4, 
                    'cd5': cd5, 
                    # 'cd6': cd6, 
                    # 'cd7': cd7, 
                    })
out.to_csv('Data\CanberraDistance.csv', index=False)
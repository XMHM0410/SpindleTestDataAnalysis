import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from NoiseReduction import kalman, wavelet
# %%计算imf分量的降噪
addr = addr = 'Data\\Fanuc6000-90\\'
dfi1 = pd.read_csv(addr+'07Circles.csv')
for i in range(dfi1.shape[1]): # 循环所有圈
    loop= dfi1[f"loop{i+1}"].values # 获得当前单圈数据
    dfi2 = pd.read_csv(addr+"IMFs\\"+f'loop{i+1}.csv') # 获取当前单圈的IMF数据
    dfi3 = pd.read_csv(addr+"IMFs\\"+f'loop{i+1}cd.csv') # 获取当前单圈IMF的改进兰氏距离
    imf_NR = {}
    for j in range(dfi2.shape[1]-1): # 获取每个IMF分量 减1为了把res去掉
        imf = dfi2[f"IMF{j+1}"].values #当前单个IMF分量
        cd = dfi3[f"IMFcd{j+1}"].values # 当前单个IMF分量的改进兰氏距离
        if j+1 <=5: # 只对前5个分量进行降噪
            if cd[0] >= 5000: # 改进兰氏距离大于等于5000
                imf_NR[f"IMFNR{j+1}"] = wavelet.Wavelet_denoise(imf)# 小波阈值降噪
                print(f"IMF{j+1} wavelet denoise over")
            elif cd[0] >= 1000 and cd[0]< 5000: # 改进兰氏距离小于5000大于1000
                imf_NR[f"IMFNR{j+1}"] = kalman.Kalman_denoise(imf)# 卡尔曼滤波
                print(f"IMF{j+1} kalman denoise over")
            else: # 改进兰氏距离小于1000
                imf_NR[f"IMFNR{j+1}"] = imf # 保持原来的信号
                print(f"IMF{j+1} denoise canceled")
        else: # 对高阶分量不降噪
            imf_NR[f"IMFNR{j+1}"] = imf # 保持原来的信号
            print(f"IMF{j+1} denoise canceled")
    print(f"loop{i+1} denoise over")
    out = pd.DataFrame(imf_NR)
    out.to_csv(addr+"IMFs\\"+f'loop{i+1}NR.csv', index=False)
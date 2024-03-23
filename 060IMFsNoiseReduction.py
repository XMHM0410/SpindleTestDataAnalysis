import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from NoiseReduction import kalman, wavelet
# %%读文件中的imf1-10
dfi2 = pd.read_csv('Data\IMFs.csv')
imf1 = dfi2["IMF1"].values
imf2 = dfi2["IMF2"].values
imf3 = dfi2["IMF3"].values
imf4 = dfi2["IMF4"].values
imf5 = dfi2["IMF5"].values
# imf6 = dfi2["IMF6"].values
# imf7 = dfi2["IMF7"].values
# %%噪声信号卡尔曼滤波 imf1
imf1_NR = kalman.Kalman_denoise(imf1)
# %%混叠信号小波阈值降噪 imf2
imf2_NR = wavelet.Wavelet_denoise(imf2)
# %%降噪结果导出
out = pd.DataFrame({'IMF1': imf1_NR,
                    'IMF2': imf2_NR, 
                    'IMF3': imf3, 
                    'IMF4': imf4, 
                    'IMF5': imf5, 
                    # 'IMF6': imf6, 
                    # 'IMF7': imf7, 
                    })
out.to_csv('Data\IMFsNoiseReduction.csv', index=False)
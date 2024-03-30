import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import plotThree,plotOne,plotPolar,plotFreq
# %% 读文件
addr = addr = 'Data\\Fanuc6000-90\\'
df = pd.read_csv(addr+'09RebuildSignal.csv')
S = df["Rebuild_S"].values
t = df["t"].values
theta = df["theta"].values
# %%读文件基本参数
dfi2 = pd.read_csv(addr+'00config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
# %%计算频谱
N = len(S)
fft_data = np.fft.fft(S) # 进行FFT变换
freq = np.fft.fftfreq(N,1/fs) # 计算对应的频率
amp = np.abs(fft_data) # 取绝对值得到幅值
amp = amp*(2/N)# 幅值转换
freq_i = freq[:len(fft_data)//2] #取正的一半
amp_i = amp[:len(fft_data)//2]
# %%plot出图
plotFreq.plotFreq(freq_i,amp_i)
plt.show()
# %%导出文件
df_out1 = pd.DataFrame({'freq':freq,'amp':amp,"fft_data":fft_data})
df_out1.to_csv(addr+'10FFT2Data.csv', index=False)
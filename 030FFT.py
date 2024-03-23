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
# %%计算频谱
N = len(S)
fft_data = np.fft.fft(S) # 进行FFT变换
freq = np.fft.fftfreq(N,1/fs) # 计算对应的频率
amp = np.abs(fft_data) # 取绝对值得到幅值
amp = amp*(2/N)# 幅值转换
freq_i = freq[:len(fft_data)//2] #取正的一半
amp_i = amp[:len(fft_data)//2]
# %%plot出图
plt.figure(figsize=(12, 6))
plt.plot(freq_i, amp_i)
plt.title('Amplitude Spectrogram')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()
# %%导出文件
df_out1 = pd.DataFrame({'freq':freq,'amp':amp,"fft_data":fft_data})
df_out1.to_csv('Data\FFTData.csv', index=False)
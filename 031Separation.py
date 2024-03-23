import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%读文件三点法混合信号
dfi1 = pd.read_csv('Data\MixedSignal.csv')
S = dfi1["S"].values
t = dfi1["t"].values
theta = dfi1["theta"].values
N = len(S)
# %%读文件基本参数
dfi2 = pd.read_csv('Data\config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
# %%读文件FFT数据
dfi3 = pd.read_csv('Data\FFTData.csv')
freq = dfi3["freq"].values
amp = dfi3["amp"].values
fft_data = dfi3["fft_data"].values
fft_data = [complex(s) for s in fft_data] #转换回复数
# %% 选取感兴趣的频率范围
interest_freq_range = (0.1, 20000.0)  # 单位为Hz
interest_freq_mask = (freq >= interest_freq_range[0]) & (freq <= interest_freq_range[1])
freq_i = freq[interest_freq_mask]
amp_i = amp[interest_freq_mask]
# %%按转速基频倍频分离同步误差和异步误
bf = rpm/60 # 基频 Hz
bf_index = np.where(freq == np.float64(bf))[0][0] #转换成索引
Sync_fft = fft_data.copy()
Async_fft = fft_data.copy()
Sync_fft[0] = 0 # 把频率为0的第一项去掉，相当于滤掉部分随机误差
Async_fft[0] = 0
for i in range(1,len(freq_i)):
    if (i) % bf_index == 0:
        Async_fft[i] = 0
    else:
        Sync_fft[i] = 0
# %%同步误差进一步分离圆度误差和偏心误差
Rod_fft = Sync_fft.copy()
Pos_fft = Sync_fft.copy()
Rod_fft[bf_index] = 0 # 圆度误差，同步误差去掉第一项
Pos_fft[bf_index] = Pos_fft[bf_index]  # 偏心误差，保留指定索引的项
Pos_fft[:bf_index] = [0] * bf_index  # 将指定索引之前的项置为0
Pos_fft[bf_index + 1:] = [0] * (len(Pos_fft) - bf_index - 1)  # 将指定索引之后的项置为0
# %%分离完的信号IFFT
Sync_sig = np.fft.ifft(Sync_fft)
Async_sig = np.fft.ifft(Async_fft)
Rod_sig = np.fft.ifft(Rod_fft)
Pos_sig = np.fft.ifft(Pos_fft)
# %%分离完信号的频谱
Sync_amp = (np.abs(Sync_fft))*(2/N)
Async_amp = (np.abs(Async_fft))*(2/N)
Rod_amp = (np.abs(Rod_fft))*(2/N)
Pos_amp = (np.abs(Pos_fft))*(2/N)
# %%误差绘图
# 同步误差
plt.figure(3)
plt.plot(theta[0:2000],Sync_sig[0:2000])
plt.title('Sync')
# 同步误差频谱
plt.figure(4)
plt.stem(freq_i, Sync_amp[interest_freq_mask])
plt.title('Sync_freq')
# 异步误差
plt.figure(5)
plt.plot(theta[0:2000],Async_sig[0:2000])
plt.title('Async')
# 异步误差频谱
plt.figure(6)
plt.stem(freq_i, Async_amp[interest_freq_mask])
plt.title('Async_freq')
plt.show()
# %%保存文件
# %%输出到文件
df1 = pd.DataFrame({'t':t,'theta':theta,
                    'Sync': np.real(Sync_sig), 
                    'Async': np.real(Async_sig), 
                    'Rod': np.real(Rod_sig), 
                    'Pos': np.real(Pos_sig)})
df1.to_csv('Data\SyncAndAsyncData.csv', index=False)
df2 = pd.DataFrame({'freq_i':freq_i,
                    'amp_i':amp_i,
                    'sync_amp':Sync_amp[interest_freq_mask],
                    'async_amp':Async_amp[interest_freq_mask],
                    'rod_amp':Rod_amp[interest_freq_mask],
                    'pos_amp':Pos_amp[interest_freq_mask]})
df2.to_csv('Data\SyncAndAsyncAmpData.csv', index=False)
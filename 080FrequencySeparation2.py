import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%读文件
dfi1 = pd.read_csv('Data\RebuildSignal.csv')
S_rebuild = dfi1["S_rebuild"].values
theta = dfi1["theta"].values
t = dfi1["t"].values
# %%定义基本参数
dfi2 = pd.read_csv('Data\config.csv')
fs = dfi2["fs"].values[0]
rpm = dfi2["rpm"].values[0]
# %%计算频谱
N = len(S_rebuild)
fft_x = np.fft.fft(S_rebuild)
freq = np.fft.fftfreq(N, d=1/fs)
amp = np.abs(fft_x)
# %%选择感兴趣的频率范围
interest_freq_range = (0.1, 20000.0)  # 单位为Hz
interest_freq_mask = (freq >= interest_freq_range[0]) & (freq <= interest_freq_range[1])
freq_i = freq[interest_freq_mask]
amp_i = amp[interest_freq_mask]
# %%找到最大幅值及对应的频率
max_amp = np.max(amp_i)
max_amp_freq = freq_i[np.argmax(amp_i)]
# %%绘制原始信号频谱幅值谱
plt.figure(2)
# plt.stem(freq[:len(freq)//2], amp[:len(amp)//2])
plt.stem(freq_i, amp_i)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Amplitude Spectrum')
plt.show()
# %%按转速基频倍频分离同步误差和异步误
bf = rpm/60 # 基频 Hz
bf_index = np.where(freq == np.float64(bf))[0][0] #转换成索引
# bf_index_range = 5 #去基频索引+-5个
# bf_index_range_list = np.arange(bf_index - bf_index_range, bf_index + bf_index_range)
Sync = fft_x.copy()
Async = fft_x.copy()
Sync[0] = 0 # 把频率为0的第一项去掉，相当于滤掉部分随机误差
Async[0] = 0
for i in range(len(freq_i)):
    if (i) % bf_index == 0:
        Async[i] = 0
    else:
        Sync[i] = 0
# %%同步误差进一步分离圆度误差和偏心误差
Rod = Sync.copy()
Pos = Sync.copy()
Rod[bf_index] = 0 # 圆度误差，去掉第一项
Pos[bf_index] = Pos[bf_index]  # 偏心误差，保留指定索引的项
Pos[:bf_index] = [0] * bf_index  # 将指定索引之前的项置为0
Pos[bf_index + 1:] = [0] * (len(Pos) - bf_index - 1)  # 将指定索引之后的项置为0
# %%分离完的信号IFFT
Sync_sig = np.fft.ifft(Sync)
Async_sig = np.fft.ifft(Async)
Rod_sig = np.fft.ifft(Rod)
Pos_sig = np.fft.ifft(Pos)
# %%分离完信号的频谱
Sync_amp = np.abs(Sync)
Async_amp = np.abs(Async)
Rod_amp = np.abs(Rod)
Pos_amp = np.abs(Pos)
# %%输出到文件
df1 = pd.DataFrame({'t':t,'theta':theta,'S_rebuild': S_rebuild,'Sync': np.real(Sync_sig), 'Async': np.real(Async_sig), 'Rod': np.real(Rod_sig), 'Pos': np.real(Pos_sig)})
df1.to_csv('Data\SyncAndAsyncDataOneLoop.csv', index=False)
df2 = pd.DataFrame({'freq_i':freq_i,'amp_i':amp_i,'sync_amp':Sync_amp[interest_freq_mask],'async_amp':Async_amp[interest_freq_mask]})
df2.to_csv('Data\SyncAndAsyncAmpDataOneLoop.csv', index=False)
# %%误差绘图
# 同步误差
plt.figure(3)
plt.plot(t[0:1000],Sync_sig[0:1000])
plt.title('Sync')
# 同步误差频谱
plt.figure(4)
plt.stem(freq_i, Sync_amp[interest_freq_mask])
plt.title('Sync_freq')
# 异步误差
plt.figure(5)
plt.plot(t[0:1000],Async_sig[0:1000])
plt.title('Async')
# 异步误差频谱
plt.figure(6)
plt.stem(freq_i, Async_amp[interest_freq_mask])
plt.title('Async_freq')
plt.show()
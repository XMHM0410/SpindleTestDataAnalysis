import pywt
import numpy as np

def Wavelet_denoise(signal, wavelet = 'db4', level = 2): # 选择默认小波基函数db4,小波分解的级别2
    coefficients = pywt.wavedec(signal, wavelet, level=level)  # 小波变换
    sigma = np.median(np.abs(coefficients[-level])) / 0.6745   # 计算噪声标准差
    threshold = sigma * np.sqrt(2 * np.log(len(signal)))       # 计算阈值
    coefficients[1:] = (pywt.threshold(i, value=threshold, mode="soft") for i in coefficients[1:])  # 阈值处理
    reconstructed_signal = pywt.waverec(coefficients, wavelet)  # 反小波变换
    return reconstructed_signal
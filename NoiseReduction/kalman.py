from filterpy.kalman import KalmanFilter
import numpy as np

def Kalman_denoise(signal):
    # 初始化卡尔曼滤波器
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.x = np.array([0., 0.])   # 初始状态向量
    kf.F = np.array([[1., 1.], [0., 1.]])  # 状态转移矩阵
    kf.H = np.array([[1., 0.]])  # 观测矩阵
    kf.P *= 1000.  # 协方差矩阵初始化
    kf.R = 5       # 测量噪声协方差矩阵
    # 使用卡尔曼滤波进行估计
    filtered_signal = []
    for z1 in signal:
        kf.predict()
        kf.update(z1)
        filtered_signal.append(kf.x[0])
    # 解决前几个数的端点问题 
    front = 15 #前10个数改成前2个数的平均值
    for i in range(0,front+1):
        filtered_signal[i] = np.mean(signal[i:3+i])
    return filtered_signal
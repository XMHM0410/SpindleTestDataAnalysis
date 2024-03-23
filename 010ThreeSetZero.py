import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %% 测量原始数据
data = pd.read_csv('Data\OriginalData.csv', header=None, delimiter='\t')
s1 = data.iloc[:, 0].values
s2 = data.iloc[:, 1].values
s3 = data.iloc[:, 2].values
# %%设置采集参数
rpm = 12000 # 转速
alpha = 84 # 探头12夹角 84
beta = 175-84 # 探头34夹角 91
fs = 200000.0 # 采样频率 Hz
# %% 三传感器信号校零转换
def set_zero(data):
    avg = np.mean(data)
    zero_data = data - avg
    return zero_data
s1 = set_zero(s1)
s2 = set_zero(s2)
s3 = set_zero(s3)
# %%输出文件
dfo1 = pd.DataFrame({"s1":s1,"s2":s2,"s3":s3})
dfo1.to_csv('Data\OriginalSignal.csv', index=False)
dfo2 = pd.DataFrame({"rpm":[rpm],"fs":[fs],"alpha":[alpha],"beta":[beta]})
dfo2.to_csv('Data\config.csv')
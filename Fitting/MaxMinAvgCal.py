import pandas as pd
import numpy as np
# %%计算最大值、最小值、平均值
def calculate_stats(data):
    max_value = np.max(data)
    min_value = np.min(data)
    avg_value = np.mean(data)
    return {"max":max_value, "min":min_value, "avg":avg_value}
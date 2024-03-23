import numpy as np

def average_denoise(data, window_size = 2):
    filtered_data = []
    for i in range(len(data)):
        if i < window_size:
            filtered_data.append(sum(data[:i+1]) / (i+1))
        else:
            filtered_data.append(sum(data[i-window_size+1:i+1]) / window_size)
    return filtered_data
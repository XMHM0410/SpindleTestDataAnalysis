import numpy as np
def canberry_distance(x,y):
    xy = np.sum( np.true_divide( np.abs(x - y), np.abs(x) + np.abs(y) ) )
    return [xy]
from matplotlib import pyplot as plt
import numpy as np
def plotPolar(theta,r,ti = "title"):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # 在极坐标图上绘制数据
    ax.plot(theta, r)
    # 设置图表的标题和标签
    ax.set_title(ti)
    # ax.set_thetagrids(np.degrees(theta[:-1]), labels=np.round(r, 2))

# # 创建一些极坐标数据
# r = np.linspace(0, 2, 100)  # r 值的数组
# theta = np.linspace(0, 2*np.pi, 100)  # theta 值的数组
# plotPolar(theta,r,"title")
# plt.show()
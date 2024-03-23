from matplotlib import pyplot as plt
def plotThree(x,y1,y2,y3,xl = "X",yl = "Y",ti = "title"):
    plt.figure(figsize=(12,6))
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(ti)
    # 图1
    plt.subplot(311)
    plt.plot(x,y1)
    # 图2
    plt.subplot(312)
    plt.plot(x,y2)
    # 图3
    plt.subplot(313)
    plt.plot(x,y3)
    plt.tight_layout()
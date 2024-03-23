from matplotlib import pyplot as plt
def plotOne(x,y,xl = "X",yl = "Y",ti = "title"):
    plt.figure(figsize=(12,6))
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(ti)
    plt.plot(x,y)
from matplotlib import pyplot as plt
def plotFreq(freq_i,amp_i,xl = "Frequency (Hz)",yl = "Magnitude",ti = "Amplitude Spectrogram"):
    plt.figure(figsize=(12, 6))
    plt.stem(freq_i, amp_i)
    plt.title(ti)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%读文件
dfi1 = pd.read_csv('Data\OneCircle.csv')
theta = dfi1["theta"].values
t = dfi1["t"].values
dfi2 = pd.read_csv('Data\IMFsNoiseReduction.csv')
imf1 = dfi2["IMF1"].values
imf2 = dfi2["IMF2"].values
imf3 = dfi2["IMF3"].values
imf4 = dfi2["IMF4"].values
imf5 = dfi2["IMF5"].values
# imf6 = dfi2["IMF6"].values
# imf7 = dfi2["IMF7"].values
# %% IMF重构
S_rebuild = np.sum([imf1,
                    imf2,
                    imf3,
                    imf4,
                    imf5,
                    # imf6,
                    # imf7,
                    ], axis=0)
# %%输出文件
out = pd.DataFrame({'t':t,'theta':theta,'S_rebuild':S_rebuild})
out.to_csv('Data\RebuildSignal.csv', index=False)
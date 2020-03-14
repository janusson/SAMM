import os
from plotnine import *
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from math import log

    # Figure Properties
xScale, yScale = [0, 10], [150, 1500]
plt.style.use("seaborn")
# sns.set(style="ticks")

    # Load dataset

    #Method 1 (Paste location):
# print("Enter file name in Figure 1 Data Folder: ")
# filename = input()

    #Method 2 (in CWD):
dataPath = r"EJ3-57-26-RA4-Sampling-2_Apex3DIons.csv"
apex3Ddf = pd.read_csv(dataPath)
plotTitle = "DTMS Map for " + dataPath.split("_")[0]

    # Define Variables
x, y, z, xyRatio = list(apex3Ddf["m_z"]), list(apex3Ddf["mobility"]*0.16), list(apex3Ddf["area"]), list(apex3Ddf["m_z"]/apex3Ddf["mobility"])
xError, yError, zError = list(apex3Ddf["errMzPPM"]), list(apex3Ddf["errArea"]), list(apex3Ddf["errMobility"])
plotdf = pd.DataFrame(zip(x, y, z, xError, yError, zError), columns = ["m/z", "DT", "Area", "m/z Error", "DT Error", "Area Error"])

""" Matplotlib Scatter
    # Colourmap settings
# cMapRange = np.arange(0, len(x))
cMapRange = np.log(z)
cBar.set_label("Signal Area")

    #Plot output
    #Fun Output: plt.scatter(x, y, s=z, c=cMapRange, edgecolor='black', cmap='plasma', linewidth=1, alpha=0.5)
plt.scatter(x, y, s=cMapRange, c=cMapRange, edgecolor='black', cmap='plasma', linewidth=1, alpha=0.5)
cBar = plt.colorbar()

    # plot labels
plt.title("DTMS Plot for " + plotTitle)
plt.xlabel("m/z")
plt.ylabel('Drift Time (ms)')
plt.tight_layout()
# plt.xscale('log')
# plt.yscale('log')
"""

"""
    # Plotnine points
cMapRange = np.log(z)
p9point = (
    ggplot(plotdf) 
    + geom_point(aes(x="m/z", y="DT", color = cMapRange, size = "Area", alpha=0.75))
    # + coord_flip()
    + labs(title = "Plot Title", x="m/z", y="DT (ms)")
)
print(p9point)
ggplot.save(p9point, plotTitle+".png")
"""



"""
### Seaborn 

# # Show the results of a linear regression within each dataset
# sns.lmplot(x="x-axis", y="y-axis", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, palette="muted", height=4,
#            scatter_kws={"s": 50, "alpha": 1})
"""
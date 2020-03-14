import os
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
plotTitle = dataPath.split("_")[0]

    # Define Variables
x, y, z = list(apex3Ddf["m_z"]), list(apex3Ddf["mobility"]*0.16), list(apex3Ddf["area"])
xError, yError, xError = list(apex3Ddf["errMzPPM"]), list(apex3Ddf["errArea"]), list(apex3Ddf["errMobility"])

    # Colourmap settings
# cMapRange = np.arange(0, len(x))
cMapRange = np.log(z)
    #Plot output
plt.scatter(x, y, s=z, c=cMapRange, edgecolor='black', cmap='plasma', linewidth=1, alpha=0.5)
# plt.scatter(x, y, s=cMapRange, c=cMapRange, edgecolor='black', cmap='plasma', linewidth=1, alpha=0.5)
cBar = plt.colorbar()

    # plot labels
plt.title("DTMS Plot for " + plotTitle)
plt.xlabel("m/z")
plt.ylabel('Drift Time (ms)')
cBar.set_label("Signal Area")

# plt.xscale('log')
# plt.yscale('log')

"""

#   3D ggplot
p = ggplot(xyzData) + geom_point(aes(x="m/z", y="Drift Time",
                                     color="Area", size="Area")) + theme_bw()
p2 = ggplot(xyzData) + geom_point(aes(x="m/z", y="Drift Time",
                                      color="Log Area", size="Area")) + theme_bw()
print(p)
print(p2)

ggplot.save(p2, "BubblePlotTest.png")




### Seaborn 

# # Show the results of a linear regression within each dataset
# sns.lmplot(x="x-axis", y="y-axis", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, palette="muted", height=4,
#            scatter_kws={"s": 50, "alpha": 1})

"""

# Figure1.py
# Python 3.7.4
# Eric Janusson
# 150320 

import os
from plotnine import *
import pandas as pd
import numpy as np
import seaborn as sns

### Load APEX3D CSV file
def getCSVFile(kwargs=None):
        # Loads dataset CSV file

    # Method 1 (Paste location):
    print("Enter CSV file path: ")
    # dataPath = input()
    print("- Disabled -")

    # Method 2 (in CWD):
    dataPath = r"D:\Programming\SAMM\SAMMplot\Experiments\EJ3-57-26-RA4-Sampling-2_Apex3DIons.csv"
    apex3Ddf = pd.read_csv(dataPath)
    print("Fetching data from: ")
    print(dataPath.split("\\")[5].split("_")[0])

    plotTitle = "DTMS Map for " + dataPath.split("\\")[5].split("_")[0]

    # Define Variables

    x, y, z, = (
        list(apex3Ddf["m_z"]),
        list(apex3Ddf["mobility"] * 0.16),
        list(apex3Ddf["area"]),
    )
    xError, yError, zError = (
        list(apex3Ddf["errMzPPM"]),
        list(apex3Ddf["errArea"]),
        list(apex3Ddf["errMobility"]),
    )
    #Export plot data:
    plotdf = pd.DataFrame(
        zip(x, y, z, xError, yError, zError),
        columns=["m/z", "DT", "Area", "m/z Error", "DT Error", "Area Error"],
    )

    return plotdf

    # Scales
data = getCSVFile()

    # Variables and errors
mz = data["m/z"]
dt = data["DT"]
area = data["Area"]
ppmError = data["m/z Error"]
dtError = data["DT Error"]
countsError = data["Area Error"]

    # Plot Scales
xScale, yScale = [0, 10], [150, 1500]
logArea, sqrtArea, linArea, recipArea, nlArea = np.log10(area), np.sqrt(area), np.exp(area), np.reciprocal(area), np.log(area)
 
from matplotlib import pyplot as plt
plt.scatter(mz, dt)
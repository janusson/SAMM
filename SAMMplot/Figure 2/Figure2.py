# Figure2.py
# Python 3.7.4
# Eric Janusson
# 150320
# Style from: https://seaborn.pydata.org/examples/regression_marginals.html
import os
from plotnine import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt

    # Custom colour scheme:
    # miami sunset
mSun = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    # maliwan divergent
malDiv = "#1e394a #7175ab #ffa7ef #ff7087 #cc6200".split(' ')
    # maliwan palette
malPal = "#1e394a #414471 #893e78 #c23a53 #cc6200".split(' ')
    # bojack gradient
bojackGrad ='#D04F6D #84486A #9C4670 #A75C87 #8C5D8B #7088B3 #71B2CA #8EE7F0 #B7F9F9 #A6F5F7'.split(" ")

def importSAMM2D(kwargs = None):
        ### Load 2D CSV files for FR, Z1, Z2
    # print("Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ") #TEST
    # userInput = input("Example: 57-24-RA2") #TEST
    userInput = r"57-24-RA2" # TEST
    basePath = r"D:\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\Experimental Data\3-57-SAMM2\2DExtract(3-57-2)"
    frMS = str(basePath + r"\Full Range\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv")
    frDT = str(basePath + r"\Full Range\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv")
    z1MS = str(basePath + r"\Z1\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv")
    z1DT = str(basePath + r"\Z1\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv")
    z2MS = str(basePath + r"\Z2\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv")
    z2DT = str(basePath + r"\Z2\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv")
    paths = [frMS, frDT, z1MS, z1DT, z2MS, z2DT]
    frScatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Fu"])
    z1Scatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Z1"])
    z2Scatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Z2"])
    frScatter = pd.concat([frScatter[0], frScatter[1]], axis=1)
    frScatter.columns = ["m/z", "Counts", "Drift Time", "Intensity"]
    return frScatter
# 2Ddata = importSAMM2D()

def importSAMM3D(kwargs = None):
        ## Load Apex3D CSV files for given experiment
    # print("Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ") #TEST
    # userInputApex = input("Example: 57-24-RA2") #TEST
    userInputApex = r"57-24-RA2" # TEST del
    apexPath = r"D:\\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\SAMM3D Extracts\APEX Output(3-57)" # TEST
    apexMS = str(apexPath + r"\Full Range\MS\EJ3-" + userInputApex + r"-Sampling-2\MZ_EJ3-" + r"-Sampling-2_Apex3DIons.csv")
    apexMS = str("D:\\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\SAMM3D Extracts\APEX Output(3-57)\EJ3-" + userInputApex + "-Sampling-2_Apex3DIons.csv")
    apexDF = pd.read_csv(apexMS)
    x, y, z, = (
        list(apexDF["m_z"]),
        list(apexDF["mobility"] * 0.16),
        list(apexDF["area"]),
    )
    xError, yError, zError = (
        list(apexDF["errMzPPM"]),
        list(apexDF["errMobility"]),
        list(apexDF["errArea"]),
    )
    newApexDF = pd.DataFrame(
        zip(x, y, z, xError, yError, zError),
        columns=["m/z", "DT", "Area", "m/z Error", "DT Error", "Area Error"])
    return newApexDF

# Data Selection
specData = importSAMM2D()
data = importSAMM3D()

    # Quick Variables
mz = data["m/z"]
dt = data["DT"]
area = data["Area"]
ppmError = data["m/z Error"]
dtError = data["DT Error"]
countsError = data["Area Error"]
print("Plotting figures...")

data.head()
trimData = data.drop(columns = ['m/z Error', 'DT Error', 'Area Error'])
# sns.pairplot(trimData)

### PLOTTING
    # Plot Regression Marginals
# sns.set(style="ticks")
# jointPlot = sns.jointplot(x = mz, y= dt,
#                 data=data,
#                 kind="kde",
#                 kind="reg",
#                 kind="resid",
#                 kind="scatter",
#                 kind="hex",
#                 # truncate=False,
#                 #   xlim=xScale,
#                 #   ylim=yScale,
#                 color="k",
#                 #   height=7
#                 )

    #MPL Style
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(2, 1, sharey=True)

# Standard plot: 
# ax.set_title("Drift Time of Mo Ions")
# ax.set_xlabel('Drift Time (ms)')
# ax.set_ylabel('Intensity')
    # dt data
# ax[0].plot(specData["Drift Time"].index, 
#         specData["Intensity"],
#         # marker='v',
#         linestyle = '--',
#         color = mSun[1]
#         )
# ax[0].set_title("Drift Time of Mo Ions")
# ax[0].set_xlabel('Drift Time (ms)')
# ax[0].set_ylabel('Intensity')
#     # ms data
# ax[1].plot(specData["m/z"], 
#         specData["Counts"],
#         color = mSun[4]
#         )
# ax[1].set_title("Mass Spectrum Mo Ions")
# ax[1].set_xlabel('m/z')
# ax[1].set_ylabel('Counts')
# plt.show()

# fig2, ax2 = plt.supplots()
# ax2.plot(specData["m/z"], 
#         specData["Counts"],
#         color = mSun[4]
#         )

# fig, ax = plt.subplots(figsize = (6, 6))
# sns.scatterplot(x= 'm/z', 
#             y = 'DT', 
#             data = data,
#             # hue = 'Area',
#             # size = 'Area Error',
#             # palette = {},
#             # xlim=(150, 1500),
#             # ylim=(1,10),
#             )
# plt.xlim(150, 1500)
# plt.ylim(2, 10)

# sns.distplot(data['DT'], kde=True, bins=300)
# sns.jointplot(x='m/z', y='DT', data=data, kind='reg')
# plt.xlim(150, 1500)
# plt.ylim(2, 10)
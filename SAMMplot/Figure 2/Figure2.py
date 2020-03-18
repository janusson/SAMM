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

def importSAMM2D(kwargs = None):
        ### Load 2D CSV files for FR, Z1, Z2
    print("Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ")
    userInput = input("Example: 57-24-RA2")
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
    print("Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ")
    userInputApex = input("Example: 57-24-RA2")
    # userInputApex = r"57-24-RA2" # TEST 
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
# importSAMM2D()
data = importSAMM3D()

    # Variables and errors
mz = data["m/z"]
dt = data["DT"]
area = data["Area"]
ppmError = data["m/z Error"]
dtError = data["DT Error"]
countsError = data["Area Error"]


function

loop

condition
filter10k = []
[mz][i],[area][i] for 

filter10k = []
for i in data["Area"]:
    if  data["m/z"] > 10000:
        print(i)



### PLOTTING
    # Plot Regression Marginals
sns.set(style="ticks")


jointPlot = sns.jointplot(x = mz, y= dt,
                data=data,
                kind="kde", 
                # truncate=False,
                #   xlim=xScale,
                #   ylim=yScale,
                color="k",

                #   height=7
                )




# hexplot = sns.jointplot(x=mz, y=dt, kind="hex", color="k")
# regular = sns.jointplot(x=mz, y=dt, kind="reg", color="k")
# residual = sns.jointplot(x=mz, y=dt, kind="resid", color="k")
# scatterplot = sns.jointplot(x=mz, y=dt, kind="scatter", color="k")



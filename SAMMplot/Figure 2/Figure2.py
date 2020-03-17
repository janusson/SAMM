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

# def importSAMM2D(kwargs = None):
### Load 2D CSV files for FR, Z1, Z2

print("Enter Experiment ID (Enter in the form: #-##-##-XX#): ")
userInput = input("Example: 57-24-RA2")
basePath = r"D:\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\Experimental Data\3-57-SAMM2\2DExtract(3-57-2)"
userInput = r"57-24-RA2"

frMS = str(basePath + r"\Full Range\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv")
frDT = str(basePath + r"\Full Range\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv")
z1MS = str(basePath + r"\Z1\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv")
z1DT = str(basePath + r"\Z1\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv")
z2MS = str(basePath + r"\Z2\MS\EJ3-" + userInput + r"-Sampling-2\MZ_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv")
z2DT = str(basePath + r"\Z2\DT\EJ3-" + userInput + r"-Sampling-2\DT_EJ3-" + userInput + r"-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv")
paths = [frMS, frDT, z1MS, z1DT, z2MS, z2DT]

# xyScatter = [msfrX, msfrY, dtfrX, dtfrY]

new = [pd.read_csv(i, skiprows=1) for i in paths]

frScatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Fu"])
z1Scatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Z1"])
z2Scatter = ([pd.read_csv(i, skiprows=1) for i in paths if os.path.lexists(i) and i[104:106] == r"Z2"])

frScatter = pd.concat([frScatter[0], frScatter[1]], axis=1)
frScatter.columns = ["m/z", "Counts", "Drift Time", "Intensity"]

    # Plot Regreassion Marginals
sns.set(style="darkgrid")
jointPlot = sns.jointplot(x = frScatter["m/z"], y= frScatter["Counts"],
                data=frScatter,
                kind="reg", 
                truncate=False,
                #   xlim=xScale,
                #   ylim=yScale,
                color="m",
                #   height=7
                )


hexplot = sns.jointplot(x=mz, y=dt, kind="hex", color="k")
regular = sns.jointplot(x=mz, y=dt, kind="reg", color="k")
residual = sns.jointplot(x=mz, y=dt, kind="resid", color="k")
scatterplot = sns.jointplot(x=mz, y=dt, kind="scatter", color="k")

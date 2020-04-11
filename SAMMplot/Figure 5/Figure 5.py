# Figure5.py
# Plot Z2 species in H2O vs. D2O reactions
# Python 3.7.4
# Eric Janusson
# 150320
import os
import pandas as pd
import numpy as np
# Custom colour schemes:
def setColourScheme():
    # miami sunset
    mSun = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    # maliwan divergent
    malDiv = '#1e394a #7175ab #ffa7ef #ff7087 #cc6200'.split(' ')
    # maliwan palette
    malPal = '#1e394a #414471 #893e78 #c23a53 #cc6200'.split(' ')
    # bojack gradient
    bojackGrad = '#D04F6D #84486A #9C4670 #A75C87 #8C5D8B #7088B3 #71B2CA #8EE7F0 #B7F9F9 #A6F5F7'.split(
        ' ')
    return(mSun, malDiv, malPal, bojackGrad)
mSun, malDiv, malPal, bojackGrad = setColourScheme()
# Data import functions (From TWIMExtract and APEX3D Output) customized to user input (default: ID: 57-24-RA2)

# 57-158-BC4
def importSAMM2D(kwargs=None):
    # Load 2D CSV files for FR, Z1, Z2
    print('Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): \n')
    userInput = input('Example: 57-158-BC4')
    basePath = r'D:\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\Experimental Data\3-57-SAMM2\2DExtract(3-57-2)'
    frMS = str(basePath + r'\Full Range\MS\EJ3-' + userInput + r'-Sampling-2\MZ_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv')
    frDT = str(basePath + r'\Full Range\DT\EJ3-' + userInput + r'-Sampling-2\DT_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#FullRange-POMSolv-Rangefile.txt_raw.csv')
    z1MS = str(basePath + r'\Z1\MS\EJ3-' + userInput + r'-Sampling-2\MZ_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv')
    z1DT = str(basePath + r'\Z1\DT\EJ3-' + userInput + r'-Sampling-2\DT_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#POMSolv-Z1-RuleFile.rul_raw.csv')
    z2MS = str(basePath + r'\Z2\MS\EJ3-' + userInput + r'-Sampling-2\MZ_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv')
    z2DT = str(basePath + r'\Z2\DT\EJ3-' + userInput + r'-Sampling-2\DT_EJ3-' +
               userInput + r'-Sampling-2_fn-1_#POMSolv-Z2-RuleFile.rul_raw.csv')
    paths = [frMS, frDT, z1MS, z1DT, z2MS, z2DT]
    frScatter = ([pd.read_csv(i, skiprows=1)
                  for i in paths if os.path.lexists(i) and i[104:106] == r'Fu'])
    frScatter = pd.concat([frScatter[0], frScatter[1]], axis=1)
    frScatter.columns = ['m/z', 'Counts', 'Drift Time', 'Intensity']
    
    z1Scatter = ([pd.read_csv(i, skiprows=1)
                  for i in paths if os.path.lexists(i) and i[104:106] == r'Z1'])
    z1Scatter = pd.concat([z1Scatter[0], z1Scatter[1]], axis=1)
    z1Scatter.columns = ['m/z', 'Counts', 'Drift Time', 'Intensity']
    
    z2Scatter = ([pd.read_csv(i, skiprows=1)
                  for i in paths if os.path.lexists(i) and i[104:106] == r'Z2'])
    z2Scatter = pd.concat([z2Scatter[0], z2Scatter[1]], axis=1)
    z2Scatter.columns = ['m/z', 'Counts', 'Drift Time', 'Intensity']
    return frScatter, z1Scatter, z2Scatter, userInput

# Create Dataframes
frScatter, z1Scatter, z2Scatter, fileID = importSAMM2D()

## Plotting
import matplotlib as mpl
from cycler import cycler
from matplotlib import pyplot as plt

msRange = [150, 1500]
dtRange = [1, 12]

#   Default MPL Settings
colors = cycler('color', mSun)

# plt.rc('figure', edgecolor='k')
plt.rc('axes', edgecolor='gray', axisbelow=False, grid=False, prop_cycle=colors)
plt.rc('grid', c='0.5', ls='-', lw=0.1)
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#003f5c')
plt.rc('lines', linewidth=0.1, aa=True)

# Mass Spectra
def plotMS(scatterData, titleCharge):
    figure1 = plt.figure(figsize=(6, 3), dpi=600)
    msLayer1 = figure1.add_axes([0.1, 0.1, 0.8, 0.8])
    # inset = figure1.add_axes([0.55, 0.65, 0.3, 0.2]) # Inset
    # inset.set_title('Mobilogram')
    # inset.plot(dtTime, dtIntensity)
    charge = str(titleCharge)
    msLayer1.set_title(charge + ' Mass Spectrum of ' + fileID, color='gray')
    msLayer1.plot(scatterData['m/z'], scatterData['Counts'])
    msLayer1.fill_between(scatterData['m/z'], 0, scatterData['Counts'], facecolor=str(mSun[0]), alpha=0.1)
    msLayer1.set_xlabel(r'$\it{m/z}$', color='gray')
    msLayer1.set_ylabel('Intensity', color='gray')
    plt.xlim(msRange)
    plt.ylim(0)
    plt.tight_layout()    
    plt.savefig("Figure5-MS-" + charge + "-" + fileID + ".png", dpi=600)
# plotMS(frScatter, 'FR')
# plotMS(z1Scatter, 'Z1')
plotMS(z2Scatter, 'Z2')

# Mobilogram (optional)
# def plotDT(scatterDatadt, dttitleCharge):
#     figure2 = plt.figure(figsize=(6, 3), dpi=600)
#     dtLayer1 = figure2.add_axes([0.1, 0.1, 0.8, 0.8])
#     # inset = figure1.add_axes([0.55, 0.65, 0.3, 0.2]) # Inset
#     # inset.set_title('Mobilogram')
#     # inset.plot(dtTime, dtIntensity)
#     charge = str(dttitleCharge)
#     dtLayer1.set_title(charge + ' Mobilogram of ' + fileID, color='gray')
#     dtLayer1.plot(scatterDatadt['Drift Time'], scatterDatadt['Intensity'], color=mSun[2])
#     dtLayer1.fill_between(scatterDatadt['Drift Time'], 0, scatterDatadt['Intensity'], facecolor=str(mSun[2]), alpha=0.1)
#     dtLayer1.set_xlabel(r'Drift Time (ms)', color='gray')
#     dtLayer1.set_ylabel('Intensity', color='gray')
#     plt.xlim(dtRange[0], dtRange[1])
#     plt.ylim(0)
#     plt.tight_layout()    
#     plt.savefig("Figure5-DT-" + charge + "-" + fileID + ".png", dpi=600)
# plotDT(frScatter, 'FR')
# plotDT(z1Scatter, 'Z1')
# plotDT(z2Scatter, 'Z2')
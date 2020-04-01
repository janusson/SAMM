# Figure2.py
# Python 3.7.4
# Eric Janusson
# 150320
# Example styles: https://seaborn.pydata.org/examples/regression_marginals.html
# https://altair-viz.github.io/gallery/scatter_marginal_hist.html

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

def importSAMM2D(kwargs=None):
    # Load 2D CSV files for FR, Z1, Z2

    # print('Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ') #TEST

    # userInput = input('Example: 57-24-RA2') #TEST

    # headers = ['Nuclearity', 'm/z', r'DT (bins)']
    # df = pd.read_csv(r'D:\2-SAMM\SAMM - Data Workup Folder\EJ3-60-SAMM3-MoMonitoring\EJ3-60 - SAMM Monitor\EJ3-60-HitList-Z2.csv', names = headers)

    userInput = r'57-158-BC4'  # TEST
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
    z1Scatter = ([pd.read_csv(i, skiprows=1)
                  for i in paths if os.path.lexists(i) and i[104:106] == r'Z1'])
    z2Scatter = ([pd.read_csv(i, skiprows=1)
                  for i in paths if os.path.lexists(i) and i[104:106] == r'Z2'])
    frScatter = pd.concat([frScatter[0], frScatter[1]], axis=1)
    frScatter.columns = ['m/z', 'Counts', 'Drift Time', 'Intensity']
    return frScatter, userInput

def importSAMM3D(kwargs=None):
    # Load Apex3D CSV files for given experiment
    # print('Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): ') #TEST
    # userInputApex = input('Example: 57-24-RA2') #TEST
    userInputApex = r'57-158-BC4'  # TEST del
    # TEST
    apexPath = r'D:\\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\SAMM3D Extracts\APEX Output(3-57)'
    apexMS = str(apexPath + r'\Full Range\MS\EJ3-' + userInputApex +
                 r'-Sampling-2\MZ_EJ3-' + r'-Sampling-2_Apex3DIons.csv')
    apexMS = str('D:\\2-SAMM\SAMM - Data Workup Folder\Data Workup (300919)\SAMM3D Extracts\APEX Output(3-57)\EJ3-' +
                 userInputApex + '-Sampling-2_Apex3DIons.csv')
    apexDF = pd.read_csv(apexMS)
    x, y, z, = (
        list(apexDF['m_z']),
        list(apexDF['mobility'] * 0.16),
        list(apexDF['area']),
    )
    xError, yError, zError = (
        list(apexDF['errMzPPM']),
        list(apexDF['errMobility']),
        list(apexDF['errArea']),
    )
    newApexDF = pd.DataFrame(
        zip(x, y, z, xError, yError, zError),
        columns=['m/z', 'DT', 'Area', 'm/z Error', 'DT Error', 'Area Error'])
    return newApexDF

# Create Dataframes
specData, fileID = importSAMM2D()
data = importSAMM3D()

# Data Processing
# 3D
dims = data[(data['m/z'] > 150) & (data['m/z'] < 1500) &
            (data['DT'] > 1) & (data['DT'] < 10) 
            # & (data['Area'] > 1)
            ]
mz, dt, area, = (dims['m/z'], dims['DT'], dims['Area'])
ppmError, dtError, countsError = (
    dims['m/z Error'], dims['DT Error'], dims['Area Error'])
# 2D
msMass, msCounts, dtTime, dtIntensity = (specData['m/z'], specData['Counts'], 
specData['Drift Time'], specData['Intensity'])
# Scales
dims[r'log(Area)'] = dims['Area'].apply(lambda x: np.log(x))
# Sort
dims.sort_values('log(Area)', inplace=True)
dims[r'Normalized log(Area)'] = (dims['log(Area)']-dims['log(Area)'].min()
                                 )/(dims['log(Area)'].max()-dims['log(Area)'].min())

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

# Blank

# 3D Plot
dtmsMap = plt.figure(figsize=(6, 6), dpi=600, facecolor='k', edgecolor='k')
dtmsLayer1 = dtmsMap.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='k')
dtmsLayer1.set_title('DTMS Map', color='gray')
dtmsLayer1.hexbin(mz, dt, 
                    C=area,
                    bins=(np.arange(len(dt))*0.2),  # Change to log for quantitative view
                    # bins='log'
                    gridsize=(250, 500),
                    # xscale='log',
                    # yscale='log'
                    # alpha=0.8,
                    # edgecolor=None
                    cmap='inferno' #'viridis' 'inferno'
                    )
dtmsLayer1.set_xlabel('$\it{m/z}$', color='gray')
dtmsLayer1.set_ylabel('Drift Time (ms)', color='gray')
dtmsLayer1.set(xlim=(msRange), ylim=(dtRange))
plt.tight_layout()
dtmsMap.savefig("Figure1cmap.png", dpi=600)
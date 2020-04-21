# Figure2-test.py
# Python 3.7.4
# Eric Janusson
# 150320
# Example styles: https://seaborn.pydata.org/examples/regression_marginals.html
# https://altair-viz.github.io/gallery/scatter_marginal_hist.html

import matplotlib.pyplot as plt
import mpl_scatter_density
from matplotlib import rcParams
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
from cycler import cycler
from matplotlib import pyplot as plt

msRange = [780, 1100]
dtRange = [30, 50]
areaMin = 1
dtTime = [num*((22.1)/200) for num in dtRange]  # time in ms

# Custom colour schemes:


def setColourScheme():
    mSun = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    malDiv = '#1e394a #7175ab #ffa7ef #ff7087 #cc6200'.split(' ')
    malPal = '#1e394a #414471 #893e78 #c23a53 #cc6200'.split(' ')
    bojackGrad = '#D04F6D #84486A #9C4670 #A75C87 #8C5D8B #7088B3 #71B2CA #8EE7F0 #B7F9F9 #A6F5F7'.split(
        ' ')
    return(mSun, malDiv, malPal, bojackGrad)


mSun, malDiv, malPal, bojackGrad = setColourScheme()
# Data import functions (From TWIMExtract and APEX3D Output) customized to user input (default: ID: 57-24-RA2)


def importSAMM2D(userInput=None):
    # Load 2D CSV files for FR, Z1, Z2
    # print('Enter EJ3-57 Experiment ID (Enter in the form: #-##-##-XX#): \n')
    # userInput = input('Example: 57-158-BC4')
    # userInput = '57-158-BC4'
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
        list(apexDF['mobility']),
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


# Create Dataframes for 2 and 3D data
# specData, z1spec, z2spec, fileID = importSAMM2D('57-158-BC4')
data = importSAMM3D()

# Data Processing
dims = data[(data['m/z'] > msRange[0]) & (data['m/z'] < msRange[1]) &
            (data['DT'] > dtRange[0]) & (data['DT'] < dtRange[1])
            & (data['Area'] > areaMin)]
mz, dt, area, = (dims['m/z'], dims['DT'], dims['Area'])

# Scales
dims[r'log(Area)'] = dims['Area'].apply(lambda x: np.log(x))
# dims[r'DT (ms)'] = data['DT'].apply(lambda x: (x*0.1105))

# Sort
dims.sort_values('Area', inplace=True)

#   Default MPL Settings
colors = cycler('color', mSun)
plt.rc('axes', edgecolor='black', axisbelow=False,
       grid=False, prop_cycle=colors)
font = {'family': 'arial',
        # 'weight' : 'bold',
        'size': 16}
plt.rc('font', **font)  # pass in the font dict as kwargs
plt.rc('figure', edgecolor='white')


def mplScatDen():
    x = dims['m/z']
    y = dims['DT']

    fig = plt.figure(figsize=(4, 4), dpi=1200)
    ax = fig.add_subplot(
        1, 1, 1, projection='scatter_density', facecolor='black')

    density = ax.scatter_density(x, y,
                                 downres_factor=4,
                                 c=dims[r'log(Area)'],
                                 cmap='magma',
                                 alpha=1
                                 )
    # ax.set_xlim(780, 1060)
    # ax.set_ylim(30, 50)
    ax.set_title('Figure 2', color='black')
    ax.set_xlabel('$\it{m/z}$', color='black')
    ax.set_ylabel('Drift Time (ms)', color='black')

    # fig.colorbar(dims[r'log(Area)'], label='Signal')
    plt.tight_layout()
    plt.show()

    fig.savefig('fig2-scatter-density-mpl.png',
                export_path='D:\Programming\SAMM\SAMMplot\Figure 2\Figure 2 - Exports\\')
    print('MPL Scatter Export Complete')
# mplScatDen()

# Plotting Axes (ms)


def mplDTMSaxes():
    # MPL HEXBIN Plot
    # dtmsMap = plt.figure(figsize=(8, 8), dpi=600, facecolor='k', edgecolor='k')
    dtmsMap = plt.figure(figsize=(8, 8), dpi=1200)
    dtmsLayer1 = dtmsMap.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='k')
    dtmsLayer1.set_title('Figure 2 Axes', color='black')

    dtmsLayer1.scatter([1, 2], [1, 2])

    dtmsLayer1.set_xlabel('$\it{m/z}$', color='black')
    dtmsLayer1.set_ylabel('Drift Time (ms)', color='black')
    # dtRange = ((12*(22.1)/200),(75*(22.1)/200))
    dtmsLayer1.set(xlim=msRange, ylim=dtTime)
    plt.tight_layout()
    dtmsMap.savefig('Figure2-axes.png',
                    export_path='D:\Programming\SAMM\SAMMplot\Figure 2\Figure 2 - Exports\\')
    print('Axes Export Complete')
# mplDTMSaxes()


# 2D Plotting
msMass, msCounts, dtTime, dtIntensity = (specData['m/z'], specData['Counts'],
                                         specData['Drift Time'], specData['Intensity'])

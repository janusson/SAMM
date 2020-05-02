# Figure4.py
# Python 3.7.4
# Eric Janusson
# 310320
import os
import pandas as pd
import numpy as np
import re
import matplotlib as mpl
from cycler import cycler
import colorcet as cc
from matplotlib import pyplot as plt
import seaborn as sns

# Custom colour schemes:


def setColourScheme():
    mSun = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    malDiv = '#1e394a #7175ab #ffa7ef #ff7087 #cc6200'.split(' ')
    malPal = '#1e394a #414471 #893e78 #c23a53 #cc6200'.split(' ')
    bojackGrad = '#D04F6D #84486A #9C4670 #A75C87 #8C5D8B #7088B3 #71B2CA #8EE7F0 #B7F9F9 #A6F5F7'.split(
        ' ')
    return(mSun, malDiv, malPal, bojackGrad)


mSun, malDiv, malPal, bojackGrad = setColourScheme()

# #   Default MPL Settings
# colors = cycler('color', malPal)
# # plt.rc('figure', edgecolor='k')
# plt.rc('axes', edgecolor='gray', axisbelow=False, grid=False, prop_cycle=colors)
# plt.rc('grid', c='0.5', ls='-', lw=0.1)
# plt.rc('xtick', direction='out', color='gray')
# plt.rc('ytick', direction='out', color='gray')
# plt.rc('patch', edgecolor='#003f5c')
# plt.rc('lines', linewidth=0.1, aa=True)

#   Default MPL Settings
colors = cycler('color', mSun)
plt.rc('axes', edgecolor='black', axisbelow=False,
       grid=False, prop_cycle=colors)
font = {'family': 'arial',
        # 'weight' : 'bold',
        'size': 16}
plt.rc('font', **font)  # pass in the font dict as kwargs
plt.rc('figure', edgecolor='white')
plt.rc('xtick', direction='out', color='k')
plt.rc('ytick', direction='out', color='k')
plt.rc('grid', c='0.5', ls='-', lw=0.1)

# SAMMtrend Solvent Experiment Data Import
data = pd.read_csv(
    r'D:\Programming\SAMM\SAMMplot\Figure 4\EJ3-57-SAMM2trends.csv', delimiter=',', header='infer')
data.reset_index()


def getSolventsFromID():
    # Organize data by experiment type (solvent used and corresponding solvent)
    pos = list(r'RA, RB, RC, RD, BA, BB, BC, BD, GA, GB, GC, GD'.split(', '))
    solv = list(
        r"H2O MeOH EtOH MeCN D2O_40 D2O_20 D2O_10 D2O_40D D2O_40G MeCNG THFG H2OG".split(' '))
    posSolv = dict(zip(pos, solv))
    exptSolv = []
    exptCond = []
    exptRegex = re.compile(r'-\D\D\d-')
    for i in range(len(data['ID'])):  # For the length of the list of experiments
        # Create regex search for vial position in experiment file titles
        mo = re.search(exptRegex, data['ID'][i])
        vialPos = list(mo.group()[1:3])  # Put positions into list
        # vialPos = vialPos[1:3]
        vialPos = ''.join(vialPos)
        solvent = posSolv[vialPos]  # Conversion to solvents
        exptSolv.append(solvent)

        condNum = int(mo.group()[3])
        exptCond.append(condNum)
    return exptSolv, exptCond

# Add reaction information to dataframe
data['Solvent'], data['Condition'] = getSolventsFromID()
solvents = 'H2O MeOH EtOH MeCN D2O_40 D2O_20 D2O_10 D2O_40D D2O_40G MeCNG THFG H2OG'.split(' ')

# add FRIMS: Z1MS+Z2MS and FRIDT: Z1DT + Z2DT
data['FRIMS'] = data['Z1MS-LWI'] + data['Z2MS-LWI']
data['FRIDT'] = data['Z1MS-LWI'] + data['Z2DT-LWI']

# Choose solvents to plot below:
solvChoose = data[
    # Aqueous
    (data['Solvent'] == 'H2O')
    # Organics
    | (data['Solvent'] == 'MeOH')
    | (data['Solvent'] == 'EtOH')
    | (data['Solvent'] == 'MeCN')
    # Deuterated Solvents
    | (data['Solvent'] == 'D2O_10')
    | (data['Solvent'] == 'D2O_20')
    | (data['Solvent'] == 'D2O_40')
    | (data['Solvent'] == 'D2O_40D')
    | (data['Solvent'] == 'D2O_40G')
    # H3PO4 Template Additive
    | (data['Solvent'] == 'H2OG')
    | (data['Solvent'] == 'MeCNG')
    | (data['Solvent'] == 'THFG')
]

# Filter out water
# if Solvent column contains H2O
aqueous = data[data.Solvent.str.contains('H2O')]
# if Solvent column doesn't contain H2O
organic = data[~data.Solvent.str.contains('2O')]

# Plotting tests
# Seaborn regression plot for charge vs solvent
# aq = sns.regplot(x='Z2MS-LWI', y='Z2DT-LWI', data=aqueous)  # High aquous variability - single solvent variable with regplot
# allSolvents = sns.lmplot(x='Z2MS-LWI', y='Z2DT-LWI', data=organic, hue='Solvent', palette='viridis')

# Z1 Top plot of water and deuterated solvents
# cmap = [bojackGrad[0], bojackGrad[2], bojackGrad[7], bojackGrad[9]]
# z1Plot = sns.lmplot(x='Z2MS-LWI', y='Z2DT-LWI',
#                     data=solvents, hue='Solvent', palette=cmap)
# Save figure
# figure4.savefig('D:\Programming\SAMM\SAMMplot\Figure 4\Figure4pair.png')

# Data process done, plot:
import seaborn as sns
data.head()
sns.regplot






































print('\n\a\a\a\a\a\a\a\a\a\aEnd\a\a\a\a\a\a\a\a\a\a\a\n')
### END OF WORKING STATE
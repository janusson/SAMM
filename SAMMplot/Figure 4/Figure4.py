# Figure4.py
# Plot results of polyoxomolybdate formation under screened reaction conditions
# Python 3.7.4
# Eric Janusson
# 310320
# Example styles: https://seaborn.pydata.org/examples/regression_marginals.html

import os
import pandas as pd
import numpy as np

# import seaborn as sns
# sns.lmplot(x='FRMS', y='FRDT', data=data)

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

# Data Import
data = pd.read_csv(
    r'D:\Programming\SAMM\SAMMplot\Figure 4\EJ3-57-SAMM2trends.csv', delimiter=',', header='infer')
    # pd.read_csv?
data.reset_index()
data.set_index("ID")


#Organize data by experiment type (solvent used)
pos = list(r'RA, RB, RC, RD, BA, BB, BC, BD, GA, GB, GC, GD'.split(', '))
solv = list(r"H2O MeOH EtOH MeCN D2O_40 D2O_20 D2O_10 D2O_40D D2O_40G MeCNG THFG H2OG".split(' '))

for i in data['ID']:
    if data[i] contains? "pos[1]":
        data['Solvent']=vialSolv
# Figure1.py
# Python 3.7.4
# Eric Janusson
# 150320

import os
import pandas as pd
import numpy as np
from cycler import cycler
from matplotlib import pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
# %matplotlib inline

# Custom colour schemes:
def setColourScheme():
    # miami sunset
    mSun = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    # maliwan divergent
    malDiv = '#1e394a #7175ab #ffa7ef #ff7087 #cc6200'.split(' ')
    # maliwan palette
    malPal = '#1e394a #414471 #893e78 #c23a53 #cc6200'.split(' ')
    # bojack gradient
    bojackGrad = '#D04F6D #84486A #9C4670 #A75C87 #8C5D8B #7088B3 #71B2CA #8EE7F0 #B7F9F9 #A6F5F7'.split(' ')
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

## Create Dataframes
specData, fileID = importSAMM2D()
data = importSAMM3D()

## Data Processing
def processData():
    # 3D
    dims = data[(data['m/z'] > 150) & (data['m/z'] < 3000) &
                (data['DT'] > 0) & (data['DT'] < 200) 
                # & (data['Area'] > 1)
                ]
    # 2D
    msMass, msCounts, dtTime, dtIntensity = (specData['m/z'], specData['Counts'], 
    specData['Drift Time'], specData['Intensity'])
    # Scales
    dims[r'log(Area)'] = dims['Area'].apply(lambda x: np.log(x))
    # Sort
    dims.sort_values('log(Area)', inplace=True)
    dims[r'Normalized log(Area)'] = (dims['log(Area)']-dims['log(Area)'].min()
                                    )/(dims['log(Area)'].max()-dims['log(Area)'].min())
    return dims
dims = processData()
mz, dt, area, = (dims['m/z'], dims['DT'], dims['Area'])
ppmError, dtError, countsError = (
    dims['m/z Error'], dims['DT Error'], dims['Area Error'])
## Plotting
msRange = (150, 1500)
dtRange = (2, 12)

#   Default MPL Settings
from matplotlib import rcParams
colors = cycler('color', mSun)
plt.rc('axes', edgecolor='black', axisbelow=False, grid=False, prop_cycle=colors)
plt.rc('grid', c='0.5', ls='-', lw=0.1)
plt.rc('xtick', direction='out', color='black')
plt.rc('ytick', direction='out', color='black')
plt.rc('patch', edgecolor='#003f5c')
plt.rc('lines', linewidth=0.18, aa=True)
font = {'family' : 'arial',
        # 'weight' : 'bold',
        'size'   : 16}
plt.rc('font', **font)  # pass in the font dict as kwargs
# plt.rc('figure', edgecolor='k')

def mplDTMS():
    # MPL HEXBIN Plot
    dtmsMap = plt.figure(figsize=(8, 8), dpi=1200, facecolor='k', edgecolor='k')
    dtmsLayer1 = dtmsMap.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='k')
    dtmsLayer1.set_title('DTMS Map', color='black')

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
    
    dtmsLayer1.set_xlabel('$\it{m/z}$', color='black')
    dtmsLayer1.set_ylabel('Drift Time (ms)', color='black')
    dtmsLayer1.set(xlim=msRange, ylim=dtRange)
    plt.tight_layout()
    dtmsMap.savefig("Figure1-cmap.png", dpi=1200)
    print('MPL Export Complete')

def dsMap():
    # Datashader 3D map
    import datashader as ds, datashader.transfer_functions as tf
    import holoviews as hv
    # from holoviews import opts
    from colorcet import bmw, bkr, bgyw, bkr, bgy, kbc, bmw, bmy, kb, bkr, CET_CBL2
    # from colorcet import bmw, isolum, 
    from matplotlib.cm import viridis, plasma, magma, inferno, cividis
    from functools import partial
    from datashader.utils import export_image
    from IPython.core.display import HTML, display
    
    # Create Canvas
    cvs = ds.Canvas(plot_width=1920//2, plot_height=1920//2, 
                    x_range=msRange, y_range=dtRange, 
                    # x_axis_type='linear', y_axis_type='linear'
                    )
    # Aggregate data
    agg = cvs.points(data, 'm/z', 'DT', ds.mean('Area'))


    cvs.points?



    # Shade
    shade = tf.shade(
        agg,
        cmap=magma,
        # cmap=bgyw, bmy,CET_CBL2,
        # color_key=None,
        how='eq_hist', # cbrt, log, linear, eq_hist
        # alpha=255,
        # min_alpha=100,
        name='DTMS Map',
    )
    #bg colour
    tf.Images(tf.set_background(shade, 'black'))
    #export figure
    # export = partial(export_image, background='black', export_path='Figure 1 - Data')
    # display(HTML('<style>.container { width:100% !important; }</style>'))
    # export(shade, 'Figure1-ds-simple')
    export_image(shade, filename='Figure1-Datashade', background='black', fmt='.png', export_path='Figure 1 - Datashade')
    print('Datashader Export Complete')

# mplDTMS()
dsMap()
cwd = str(os.getcwd())
print(r'Export Complete to: *-_-_-_-* ' + cwd + ' *-_-_-_-*')
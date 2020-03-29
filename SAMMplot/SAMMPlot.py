# SAMMPlot.py
# Python 3.7.4 
# Eric Janusson 
# 270320
import os
import pandas as pd
import numpy as np
# %matplotlib inline

    ### Seaborn Style 
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style='ticks')
# cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
# ax = sns.scatterplot(x='m/z', 
#                 y='DT',
#                 data=dims,
#                 hue='Area',
#                 # hue_norm=(0, 100),
#                 size='Area',
#                 sizes=(20, 200),
#                 linewidth=0,
#                 edgecolor=None,
#                 alpha=0.60,
#                 palette=cmap
#                 )

# plt.xlabel('$\it{m/z}$')
# plt.ylabel('Drift Time (ms)')
# plt.show()

    #Extra parameters:
                # style=area,
                # hue=area, 
                # size=None, 
                # data=trimData, 
                # palette=None, 
                # hue_order=None, 
                # hue_norm=None, 
                # sizes=None, 
                # size_order=None, 
                # size_norm=None, 
                # markers=True, 
                # style_order=None, 
                # x_bins=None, 
                # y_bins=None, 
                # units=None, 
                # estimator=None, 
                # ci=95, 
                # n_boot=1000, 
                # alpha="auto", 
                # x_jitter=None, 
                # y_jitter=None, 
                # legend="brief", 
                # ax=None


    ## MPL Style
    
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, sharey=True)

## Standard plot: 
ax.set_title('Drift Time of Mo Ions')
ax.set_xlabel('Drift Time (ms)')
ax.set_ylabel('Intensity')
    dt data
ax[0].plot(specData['Drift Time'].index, 
        specData['Intensity'],
        # marker='v',
        linestyle = '--',
        color = mSun[1]
        )
ax[0].set_title('Drift Time of Mo Ions')
ax[0].set_xlabel('Drift Time (ms)')
ax[0].set_ylabel('Intensity')
    # ms data
ax[1].plot(specData['m/z'], 
        specData['Counts'],
        color = mSun[4]
        )
ax[1].set_title('Mass Spectrum Mo Ions')
ax[1].set_xlabel('m/z')
ax[1].set_ylabel('Counts')
plt.show()

fig2, ax2 = plt.supplots()
ax2.plot(specData['m/z'], 
        specData['Counts'],
        color = mSun[4]
        )

fig, ax = plt.subplots(figsize = (6, 6))
sns.scatterplot(x= 'm/z', 
            y = 'DT', 
            data = data,
            # hue = 'Area',
            # size = 'Area Error',
            # palette = {},
            # xlim=(150, 1500),
            # ylim=(1,10),
            )
plt.xlim(150, 1500)
plt.ylim(2, 10)

sns.distplot(data['DT'], kde=True, bins=300)
sns.jointplot(x='m/z', y='DT', data=data, kind='reg')
plt.xlim(150, 1500)
plt.ylim(2, 10)


    ### ggplot Style
# import plotnine
# from plotnine import ggplot, geom_point, aes, theme_bw
# ax = ggplot(dims) + geom_point(aes(x = "m/z", y = "DT", color = r"log(Area)", size = "Area")) + theme_bw()
# print(ax)

import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Set plotting style
sns.set(style='ticks')
plt.style.use('seaborn')

# Load dataset

    # print("Enter file name in Figure 1 Data Folder: ")
    # filename = input()
df = pd.read_csv(r"EJ3-57-26-RA4-Sampling-2_Apex3DIons.csv")
df.head()


xScale, yScale = [0, 10], [150, 1500]
# plt.plot(xScale, yScale)

# sns.lmplot(x="m/z", y= 'y', col='Col', hue='dataset', data=df)


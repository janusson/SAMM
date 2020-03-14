import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


    # Figure Properties
xScale, yScale = [0, 10], [150, 1500]
plt.style.use('ggplot')
sns.set(style='ticks')

    # Load dataset
#Method 1 (Paste location):
# print("Enter file name in Figure 1 Data Folder: ")
# filename = input()
#Method 2 (in CWD):
df = pd.read_csv(r"EJ3-57-26-RA4-Sampling-2_Apex3DIons.csv")

    # Organize data
df.head()
x = df["m_z"]
y = 






# Show the results of a linear regression within each dataset
sns.lmplot(x="x-axis", y="y-axis", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})


# xyzData = rawData[['3D_m_z', '3D_Intensity', '3D_TC']].rename(columns={'3D_m_z': 'm/z', '3D_Intensity': 'Area', '3D_TC': 'Drift Time'}) #note: applicable to APEX outs from Driftscope. Non DS exports use different XYZ headers
xyzData = rawData[['m_z', 'inten', 'area', 'mobility']].rename(
    columns={'m_z': 'm/z', 'inten': 'Intensity', 'area': 'Area', 'mobility': 'Drift Time'})
#   Import 2D Data
dtData = pd.read_csv(
    r'S:\S-SAMM Programs\SAMM\SAMMplot\SAMMPlotData\DT_EJ3-52-A2-9-BA7-Sampling.csv', skiprows=[0, 1])
dtData.columns = ["Drift Time", "Intensity"]

mzData = pd.read_csv(
    r'S:\S-SAMM Programs\SAMM\SAMMplot\SAMMPlotData\MZ_EJ3-52-A2-9-BA7-Sampling.csv', skiprows=[0, 1])
mzData.columns = ["m/z", "Intensity"]

#   Process: Sort all data by X, add Log scale
xyzData.sort_values(["m/z"], inplace=True)
dtData.sort_values(["Drift Time"], inplace=True)
mzData.sort_values(["m/z"], inplace=True)
xyzData["Log Area"] = np.log(xyzData["Area"])

xyzData.head()
mzData.head()
dtData.head()

#   Quickcheck plots
plt.plot(dtData["Drift Time"], dtData["Intensity"])
plt.plot(mzData["m/z"], mzData["Intensity"])
plt.hist2d(xyzData["m/z"], xyzData["Drift Time"], bins=100)

#   3D ggplot
p = ggplot(xyzData) + geom_point(aes(x="m/z", y="Drift Time",
                                     color="Area", size="Area")) + theme_bw()
p2 = ggplot(xyzData) + geom_point(aes(x="m/z", y="Drift Time",
                                      color="Log Area", size="Area")) + theme_bw()
print(p)
print(p2)

ggplot.save(p2, "BubblePlotTest.png")

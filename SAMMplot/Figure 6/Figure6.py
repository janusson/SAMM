## Regression analysis
# https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
# %matplotlib inline

# sklearnData = data.drop(columns=['m/z Error', 'DT Error', 'Area Error']).sort_values(by='Area').reset_index()

# sns.distplot(sklearnData['Area'])
# sklearnData.describe()

# x = sklearnData['m/z'].values.reshape(-1, 1)
# y = sklearnData['DT'].values.reshape(-1, 1)
# xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=0)
# regresso = LinearRegression()
# regresso.fit(xTrain, yTrain) #Training the algorithm

# yPred = regresso.predict(xTest)
# df = pd.DataFrame({'Actual': yTest.flatten(), 'Predicted':yPred.flatten()})

# # Residuals
# df1 = df.head(25)
# df1.plot(kind='bar', figsize=(6,4))
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

# plt.scatter(xTest, yTest, color=mSun[0], alpha=0.05, edgecolor=None)
# plt.plot(xTest, yPred, color='red', linewidth=1)
# plt.show()

# print(regresso.intercept_)
# print(regresso.coef_)
# print('Root-Mean-Squared Error: ', np.sqrt(metrics.mean_squared_error(xTest, yPred)))

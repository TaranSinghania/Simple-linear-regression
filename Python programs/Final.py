#importing all packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
#refer to the document titled 'splitting and exporting datasets' for code for the same
#Importing training dataset
data=pd.read_csv('C:/Users/taran/OneDrive/Desktop/Datasets/train.csv')
data.shape
data.head()
X=data['Decimaldate'].values
Y=data['CO2_Final'].values
#Calculating slope parameter and intercept[b1, b0]
mean_X=np.mean(X)
mean_Y=np.mean(Y)
m=len(X)
num=0
den=0
for i in range(m):
	   num+=(X[i] - mean_X) * (Y[i] - mean_Y)
	   den+=(X[i] - mean_X) ** 2
b1=num/den
b0=mean_Y-(b1*mean_X)
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
#Using values of b1 and b0 to find rmse
data=pd.read_csv('C:/Users/taran/OneDrive/Desktop/Datasets/test.csv')
X=data['Decimaldate'].values
Y=data['CO2_Final'].values
mean_X=np.mean(X)
mean_Y=np.mean(Y)
m=len(X)
rmse = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/m)
print('RMSE: %.3f' % (rmse))
#Finding R^2
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_Y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print('R^2: %.3f'%(r2))
#Plotting graph using matplotlib
max_x = np.max(X)+10
min_x = np.min(X)-10
x = np.linspace(min_x, max_x, 50)
y = b0 + b1 * x
#Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
#Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Decimal Date')
plt.ylabel('CO2')
plt.legend()
plt.show()
#we can use the graph to predict values






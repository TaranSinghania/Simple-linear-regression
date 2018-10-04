#importing all packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
#importing main csv file on to python
data=pd.read_csv('C:/Users/taran/OneDrive/Desktop/Datasets/archive.csv')
data.head()
data.shape
#Splitting into training and testing dataset
y=data['CO2Useason_adjusted'].values
x=data.drop('CO2Useason_adjusted', axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#Exporting dataset to csv(test)
res=x_test
my_df=pd.DataFrame(res)
my_df.to_csv('test.csv', index=False, header=False)
my_df.shape
#Exporting dataset to csv(train)
res=x_train
my_df=pd.DataFrame(res)
my_df.to_csv('train.csv', index=False, header=False)
my_df.shape

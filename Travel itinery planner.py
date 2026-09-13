# Import Libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
data = pd.read_csv('Weather Dataset.csv')
data.head(5)
data.info()
data.isnull().sum()
mean_temp = np.var(data['Temperature (c)'])
print("Mean Temperature is :", mean_temp)
var_temp = np.mean(data['Temperature (c)'])
print("variation of Temperature is:", var_temp)
standard_deviation_temp = np.std(data['Temperature (c)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)
for i in range(1, 13):
    month = data.loc[data["month"] == i] ["Temperature (c)"]
    print("For month" +str(i))
    print("Mean temperature is" + str(np.mean(month)))
    print("Standard deviation is" + str(np.std(month)) +"\n")
import numpy as np
from numpy import random
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

#%%
address = 'C:/Users/___/.csv'
#%%
cars = pd.read_csv(address)
cars.columns = ['car names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']

#%%
# Creating a Line Chart
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(x,y)
#%%
mpg = cars['mpg']
mpg.plot()
#%%
df = cars[['cyl','wt','mpg']]
df.plot()
#%%
# Creating a Bar Chart
plt.bar(x,y)
#%%
mpg.plot(kind='bar')
#%%
mpg.plot(kind='barh')
#%%
# Creating a Pie Chart
z = [1,2,3,4,0.5]
plt.pie(z)
plt.show()

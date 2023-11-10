import pandas as pd
import numpy as np
from pandas import Series, DataFrame

import scipy
from scipy import stats

#%%
address = 'C:/Users/____.csv'
cars = pd.read_csv(address) 
cars.columns = ['car names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']
#%%
print(cars.sum())
sum_row = cars.sum(axis=1)
print(sum_row)
#%%
print(cars.median())
#%%
print(cars.mean())
#%%
print(cars.max())
#%%
mpg = cars.mpg
print(mpg.idxmax())
#%%
print(cars.var())
#%%
gear = cars.gear
print(gear.value_counts())
#%%
print(cars.describe())

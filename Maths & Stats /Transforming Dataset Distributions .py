import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import scale

plt.style.use('seaborn-whitegrid')
#%%
address = 'C:/Users/___.csv'
cars = pd.read_csv(address) 
cars.columns = ['car_names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']
cars.index = cars.car_names
#%%
mpg = cars.mpg
plt.plot(mpg)
#%%
print(cars[['mpg']].describe())
#%%
mpg_matrix = mpg.values.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

#%%
scaled = preprocessing.MinMaxScaler(feature_range=((0,10)))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
#%%
standardised_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standardised_mpg)

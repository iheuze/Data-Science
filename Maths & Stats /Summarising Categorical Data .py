import pandas as pd
address = 'C:/Users/____.csv'
cars = pd.read_csv(address) 
cars.columns = ['car_names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']
cars.index = cars.car_names
#%%
carb = cars.carb
print(carb.value_counts())
#%%
cars_cat = cars[['cyl','vs','am','gear','carb']]
print(cars_cat.head())
#%%
gears_group = cars_cat.groupby('gear')
print(gears_group.describe())
#%%
#transforming variables to categorical data type
cars['group'] = pd.Series(cars.gear, dtype='category')
print(cars['group'].dtypes)
#%%
print(cars['group'].value_counts())

#%%
#describing data with crosstabs
print(pd.crosstab(cars['am'], cars['gear']))

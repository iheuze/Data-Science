import pandas as pd
address = 'C:/Users/___.csv'

cars = pd.read_csv(address)
#%%
cars.columns = ['car names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']
print(cars.head())
#%%
car_group = cars.groupby(cars['cyl'])
print(car_group.mean())

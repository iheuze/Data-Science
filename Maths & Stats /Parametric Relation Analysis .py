import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats.stats import pearsonr

plt.style.use('seaborn-whitegrid')
#%%
address = 'C:/Users/____.csv'
cars = pd.read_csv(address) 
cars.columns = ['car_names', 'mpg', 'cyl', 
                'disp', 'hp', 'drat', 'wt',
                'qsec', 'vs', 'am', 'gear',
                'carb']
cars.index = cars.car_names
#%%
sb.pairplot(cars)
#%%
x = cars[['mpg','hp','qsec','wt']]
sb.pairplot(x)
#%%
mpg=cars['mpg']
hp=cars['hp']
qsec=cars['qsec']
wt=cars['wt']

pearsonr_coefficient, pvalue = pearsonr(mpg, hp)
print('Pearson R Correlation Coefficient %0.3f'% (pearsonr_coefficient))
#%%
pearsonr_coefficient, pvalue = pearsonr(mpg, qsec)
print('Pearson R Correlation Coefficient %0.3f'% (pearsonr_coefficient))
#%%
pearsonr_coefficient, pvalue = pearsonr(mpg, wt)
print('Pearson R Correlation Coefficient %0.3f'% (pearsonr_coefficient))
#%%
#using pandas
corr = x.corr()
print(corr)
#%%
#using seaborn
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)

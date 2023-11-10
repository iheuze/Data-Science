import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import chi2_contingency
from scipy.stats.stats import spearmanr

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
x = cars[['cyl','vs','am','gear']]
sb.pairplot(x)
#%%
cyl=cars['cyl']
vs=cars['vs']
am=cars['am']
gear=cars['gear']

spearmanr_coefficient, pvalue = spearmanr(cyl, vs)
print('Spearman R Correlation Coefficient %0.3f'% (spearmanr_coefficient))
#%%
spearmanr_coefficient, pvalue = spearmanr(cyl, am)
print('Spearman R Correlation Coefficient %0.3f'% (spearmanr_coefficient))
#%%
spearmanr_coefficient, pvalue = spearmanr(cyl, gear)
print('Spearman R Correlation Coefficient %0.3f'% (spearmanr_coefficient))
#%%
table = pd.crosstab(cyl, am)
chi2, p, dof, expected = chi2_contingency(table.values)
print(chi2, p)
#%%
table1 = pd.crosstab(cyl, vs)
chi2, p, dof, expected = chi2_contingency(table1.values)
print(chi2, p)
#%%
table2 = pd.crosstab(cyl, gear)
chi2, p, dof, expected = chi2_contingency(table2.values)
print(chi2, p)

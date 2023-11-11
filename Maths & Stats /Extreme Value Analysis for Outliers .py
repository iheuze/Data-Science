import pandas as pd
import matplotlib.pyplot as plt

#%%
address = 'C:/Users/____.csv'
df = pd.read_csv(address) 
df.columns = ['Sepal Length', 'Sepal Width', 
                'Petal Length', 'Petal Width',
                'Species']

#%%
x = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

print(df[:5])

#%%
df.boxplot(return_type='dict')
plt.plot()
#%%
sepal_width = x[:,1]
iris_outliers=(sepal_width > 4)
print(df[iris_outliers])
#%%
sepal_width = x[:,1]
iris_outliers=(sepal_width < 2.05)
print(df[iris_outliers])
#%%
#applying tukey labelling
pd.options.display.float_format = '{:.1f}'.format
x_df = pd.DataFrame(x)
print(x_df.describe())

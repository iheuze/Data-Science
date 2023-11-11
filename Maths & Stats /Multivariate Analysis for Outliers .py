import pandas as pd
import seaborn as sb

#%%
address = 'C:/Users/_____.csv'
df = pd.read_csv(address, header=None, sep=',') 
df.columns = ['Sepal Length', 'Sepal Width', 
                'Petal Length', 'Petal Width',
                'Species']

#%%
data = df.iloc[:, 0:4].values
target = df.iloc[:, 4].values

print(df[:5])

#%%
sb.boxplot(x='Species', y='Sepal Length', data=df, palette='Set3')

#%%
# Look at scatterplot matrix

sb.pairplot(df, hue='Species', palette='Pastel1')

import pandas as p
import matplotlib.pyplot as plt
#%%
address = 'C:/Users/isabe/Documents/LinkedIn Learning/Ex_Files_Python_Data_Science_EssT_Pt_1/Exercise Files/Data/Superstore-Sales.csv'
df = pd.read_csv(address, index_col='Order Date', 
                 encoding='cp1252', parse_dates=True) 
#%%
print(df.head())
#%%
df['Order Quantity'].plot()
#%%
df2 = df.sample(n=100, random_state=25, axis=0)

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()

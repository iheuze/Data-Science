from pandas import DataFrame
#%%
DF_obj = DataFrame({'column 1':[1,1,2,2,3,3,3],
                    'column 2':['a','a','b','b','c','c','c'],
                    'column 3':['A','A','B','B','C','D','C']})
print(DF_obj)
#%%
print(DF_obj.duplicated())
#%%
print(DF_obj.drop_duplicates())
#%%
print(DF_obj.drop_duplicates(['column 3']))
print(DF_obj.drop_duplicates(['column 2']))

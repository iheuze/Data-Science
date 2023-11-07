import numpy as np
import pandas as pd
from pandas import Series, DataFrame

DF_obj = DataFrame(np.arange(36).reshape((6,6)))
print(DF_obj)
#%%
DF_obj_2 = DataFrame(np.arange(15).reshape((5,3)))
print(DF_obj_2)

#%%
#concatenating data
print(pd.concat([DF_obj, DF_obj_2], axis=1))
#%%
print(pd.concat([DF_obj, DF_obj_2]))
#%%
#dropping data
print(DF_obj.drop([0,2]))
#%%
print(DF_obj.drop([0,2], axis=1))
#%%
#adding data
series_obj = Series(np.arange(6))
series_obj.name = "added variable"
print(series_obj)
#%%
variable_added = DataFrame.join(DF_obj, series_obj)
print(variable_added)
#%%
added_datatableF = variable_added.append(variable_added, ignore_index=False)
print(added_datatableF)
#%%
added_datatableT = variable_added.append(variable_added, ignore_index=True)
print(added_datatableT)
#%%
#sorting data
DF_sorted = DF_obj.sort_values(by=(5), ascending=[False])
print(DF_sorted)

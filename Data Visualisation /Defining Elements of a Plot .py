import numpy as np
from numpy import random
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#%%
#defining axes, ticks, and grids
x = range(1,10)
y = y = [1,2,3,4,0,4,3,2,1]
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

ax.plot(x, y)
#%%
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

ax.plot(x, y)
#%%
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

ax.grid()

ax.plot(x, y)
#%%
fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x)
ax2.plot(x, y)

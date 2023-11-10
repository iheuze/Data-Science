import numpy as np

np.set_printoptions(precision=2)
#%%
aa = np.array([[2.,4.,6.],[1.,3.,5.],
               [10.,20.,30]])
print(aa)

bb = np.array([[0.,1.,2.],[3.,4.,5.],
               [6.,7.,8]])
print(bb)
#%%
print(aa*bb)    #not matrix multiplication
#%%
print(np.dot(aa,bb))    #matrix multiplication

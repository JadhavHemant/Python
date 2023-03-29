import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data=[1,2,3,4,5,6,7,8]
dt=np.array(data)
print(dt)

# dt=pd.Series(data)
# print(dt)    #SHOW INDEX NUMBER

# dt=pd.Series(data,index=[1,2,3,4,5,6,7,8])
# print(dt)      #USER DEFINE INDEX

dt=pd.Series(data,index=['a','b','c','d','e','f','g','h'])
print(dt)
print(dt['g'])


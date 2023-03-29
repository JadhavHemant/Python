import numpy as np
from scipy import stats

data=np.array([[10,20,30],[40,23,43],[12,23,56]])
x=np.mean(data)
print(x)
x=np.median(data)
print(x)
data1=[1,2,3,4,5,6,6,7,6,88,7,5,4,5,64,65,32]
x=stats.mode(data1)
print(x)


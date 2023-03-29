import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
d1=np.random.randn(10,4)
d2=pd.date_range('01/01/2023',periods=10)

x=pd.DataFrame(d1,index=d2)

x.plot()
plt.show()

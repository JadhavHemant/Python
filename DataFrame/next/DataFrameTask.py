import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data={
    "product_name":["pen","pencile","sugar","soap","pen","pencile","sugar","soap","pen","pencile","sugar","soap"],
    "years":[2010,2010,2010,2010,2011,2011,2011,2011,2012,2012,2012,2012],
    "profit":[10000,2400,2340,3245,5432,5665,3465,100,2341,4564,1019,1001]
      }


df=pd.DataFrame(data)
# print(df)
new=df.groupby(["product_name"]) 

for groupa , d in new:
    #  print(groupa)
    #  print(d)
    a=np.array(groupa)
    b=np.array(d)
    print(b)
    print(a)


pro=df.groupby("years")
for groupb,i in pro:
    print(groupb)
    print(i)
    y=np.array(groupb)
    x=np.array(i)
    
print("Year Wise",x)    

pro=df.groupby("profit")
for groupc,x in pro:
    print(groupc)
    print(x)
    h=np.array(x)


product=input("enter any product")
product_g=df[df['product_name']==(product)]
plt.plot(product_g['years'],product_g['profit'])
df.plot()
plt.show()
# y=pd.DataFrame(y,x)
# y.plot()
# plt.show()   
 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
rno=[1,2,3,4,5]
name=["Ajay","Amit","Suresh","Sunil","Deepak"]
eng=[12,54,27,45,34]
math=[28,89,27,56,89]
sci=[23,67,48,45,67]
st={"rno":rno,"name":name,"maths":math,"science":sci,"english":eng}
df=pd.DataFrame(st,columns=["rno","name","english","maths","science"])
print(df)
df["total"]=df["english"]+df["maths"]+df["science"]
print(df)
df["percentage"]=df["total"]/3
print(df)
# df.plot("rno","english")
df["result"]=df["percentage"].apply(lambda x:'Pass' if x>=40 else 'Fail')
print(df)
df["english result"]=df["english"].apply(lambda x:'Pass' if x>=35 else 'Fail')
print(df)
df["maths result"]=df["maths"].apply(lambda x:'Pass' if x>=35 else 'Fail')
print(df)
df["science result"]=df["science"].apply(lambda x:'Pass' if x>=35 else 'Fail')
print(df)
# df.plot("rno","maths")
# df.plot("rno","english")
plt.show()

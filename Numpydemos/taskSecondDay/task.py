import numpy as np
from matplotlib import pyplot as plt
r=[]
m=[]
i=1
while(i!=0):
    a=int(input("Enter Roll-Number Here : "))
    b=int(input("Enter Marks Here : "))

    r.append(a)
    m.append(b)
    i=int(input("Do You Want Add More Roll-Numbers ? yes(1)/no(0)"))
x=np.array(r)
y=np.array(m)  

plt.plot(x,y,"or")
plt.show()
f=open("square.txt","w")
x=1
for x in range(1,101):
    f.write("square of :=" +str(x)+"="+str(x*x) +"\n")
f.close()
print("finish")
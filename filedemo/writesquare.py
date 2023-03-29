f=open("squares.txt","a")
i=1
for i in range(1,101):
    f.write("Square of "+str(i)+" = "+str(i*i)+"\n")

f.close()
print("Finished")
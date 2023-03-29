f=open("square.txt","r")
data=f.read()
count=0
for d in data:
    if(d=="1"):
        count+=1
print(str(count))

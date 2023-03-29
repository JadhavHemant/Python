import os
data=os.listdir("C:\\Users\\Dell PC\\OneDrive\\Documents")
cnt=0
for d in data:
    if "v" in d:
        cnt+=1
    print(d)        
print(cnt)     
































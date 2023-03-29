i=1
while i < 100:
    print(i)
    if(i==9):
       break
    i +=1   


print("------------------------------------<Rverse>-----------------------------------------")
a = 10
while a>0:
    print(a)
    if(a==1):
        break
    a -=1    


print("------------------------------------<Skip>-----------------------------------------")
i = 0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


print("------------------------------------<no longer>-----------------------------------------")
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer")

print("------------------------------------<print name>-----------------------------------------")

a=0
while a<3:
    a=a+1
    print("hello")

print("------------------------------------<while loop with continue(remove char)>-----------------------------------------")
i=0
a="hemantjadhav"
while i<len(a):
    if a[i]=='t' or a[i]=='a':
        i+=1
        continue
    print(a[i])
    i+=1



print("------------------------------------<breack and continue(remove between)>-----------------------------------------")

i=0
a="hemant jadhav"
while i<len(a):
    if a[i]=='t' or a[i]=='j':
        i+=1
        break
    print(a[i])
    i+=1

print("------------------------------------<count number()>-----------------------------------------")
i=0
a="hemant jadhav"
while i<len(a):
    i+=1
    pass
print(i)

print("------------------------------------<while loop with else>-----------------------------------------")
i=0
while i<4:
    i+=1
    print(i)
else:
    print("no break")
i=0
while i<4:
    i+=1
    print(i)
else :
    print("no break")        


print("------------------------------------<>-----------------------------------------")






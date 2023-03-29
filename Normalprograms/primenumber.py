n=int(input("Enter Any Number "))
count=0
for i in range(2,n):
    if(n%i==0):
     count=count+1
if (count==0):
    print("prime Number")
else:
    print("Not Prime number")
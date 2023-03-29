# create list 
mylist=[1,2,3,4,5,6,7,8,9] #list can store  integer
mylist1=["hello","world","hiii"] #list can store string 
mylist2=["hello",40,True] #list can store multipale data type value
print(mylist,mylist1,mylist2)
print(mylist2+mylist)
for i in range(len(mylist)):
    print(i)
for j in range(1,len(mylist)):
    if j%2==0:
        print(j)
mylist1.clear()
print(mylist1)
del mylist
print(mylist)
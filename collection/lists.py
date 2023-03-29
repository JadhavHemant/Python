# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

mylist=[1,2,3,4,5,6,7,8,9]
print(mylist)
print(mylist[-2])
print(len(mylist))
print(type(mylist))
print(mylist[2:5])
print(mylist[:5])
print(mylist[2:])
print(mylist[-4:-1])
if 5 in mylist:
    print("yes")
mylist.insert(2,"hello")
print(mylist)    
mylist.append("orange")
print(mylist)


xyz=list(("heman","jojo","nibba","beta"))
print(xyz)
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
     print(thislist[i])



list1=["hello","i","am","hemant"]
list2=["how","are","you"]
list1.extend(list2)
print(list1)


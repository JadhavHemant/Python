# creation of list
mylist=[1,2,3,4,5,6,7,8,9,0]
print(mylist)



#list iteams access
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
print(mylist[6])
print(mylist[7])
print(mylist[8])
print(mylist[9])



#Access  list index numbers using for loop
for i in range(0,len(mylist)):
    print(i)

#finding list length
print(len(mylist))

#finding list datatype
print(type(mylist))

# list contain multiple datatyes objects 
# duplicate data also allowcate

mylist1=["hello",1,True,"world"]
print(mylist1)

print(type(mylist1[0]))
print(type(mylist1[1]))
print(type(mylist1[2]))
print(type(mylist1[3]))

#show the data of list type()

print(type(mylist))
print(type(mylist1))


#linked list 
linked=list(("hemant","balkrushna","jadhav"))
print(linked)

# positive Access using index 
number=[1,2,3,4,5,6,7,8,9,0,"hello","world","welcome","to","python"]
print(number)
print(number[0])
print(number[1])
print(number[2])
print(number[3])
print(number[4])
print(number[5])
print(number[6])
print(number[7])
print(number[8])
print(number[9])
print(number[10])
print(number[11])
print(number[12])
print(number[13])
print(number[14])


# negative Access using index (here starting index is "-1")

print(number)
print(number[-1])
print(number[-2])
print(number[-3])
print(number[-4])
print(number[-5])
print(number[-6])
print(number[-7])
print(number[-8])
print(number[-9])
print(number[-10])
print(number[-11])
print(number[-12])
print(number[-13])
print(number[-14])
print(number[-15])



#range of index


#print the third and fourth fifth value in list
print(number[2:5])


# printing first 5 valus in list

print(number[ :5]) 


#printing after values of the pass pumber
print(number[2:])

#check iteam exist in list or not
print(number)
if "python" in number:
    print("yes")
else:
    print("no")    


#change list iteams for specific index iteam

number[1]="cherry"
print(number)


#insert iteam in list
number.insert(1,"hello")
print(number)


#extend list
# to append elements from another list the to the current list using extends


mylist.extend(number)
print(mylist)

mylist.append(number)
print(mylist)




# remove element from list
mylist2=["hello","world","new"]
mylist2.remove("hello")
print(mylist2)

#delete whole list 
del mylist2
print(mylist2)



# remove specipic index from list
mylist2.pop(1)
print(mylist2)














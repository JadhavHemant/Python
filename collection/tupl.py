# create tuple

hemant = ("apple", "banana", "cherry")
print(hemant)

# tuple can contain dulicte values

hemant = ("apple", "banana", "cherry","apple","banana")
print(hemant)

# find the tuple lenth using len() function

hemant = ("apple", "banana", "cherry","apple","banana")
print(len(hemant))


#create tuple with one iteam
# remember the comma:

tupleone=("apple",)
print(type(tupleone))

# tuple carry any data type

integer=(1,2,3,4,5,6,7,8,9)
print(type(integer[1]))
print(type(integer))

string=("hello","world","hii")
print(type(string[1]))
print(type(string))

boolean=(True,False,False)
print(type(boolean[1]))
print(type(boolean))


# A tuple can contain different data types:
Alldatatypes = ("abc", 34, True, 40, "male")
print(type(Alldatatypes))

# type()

tupleone=("apple",)
print(type(tupleone))


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
this = tuple(("apple", "banana", "cherry"))
print(this)



# Access Tuple Items

integer=(1,2,3,4,5,6,7,8,9)
print(integer[1])
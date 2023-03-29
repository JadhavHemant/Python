# print("=====================(count of number)======================")

# import math
# cnt=0
# n=int(input("Enter any number"))
# while(n!=0):
#     cnt=cnt+1
#     n=math.floor(n/10)
# print("total digits="+str(cnt))    

# print("============================(reverse number)====================")

# import math
# sum=0
# n=int(input("enter any number:"))
# while(n!=0):
#   rem=n%10
#   sum=rem+sum*10
#   n=math.floor(n/10)
# print(str(sum))


# print("==============================(             )==============================")

# import math
# sum=0
# n=int(input("enter any number:"))
# x=n
# while(n!=0):
#   rem=n%10
#   sum=rem+sum*10
#   n=math.floor(n/10)
# print(str(sum))
# if(sum==x):
#     print("number is palindrome")
# else:
    # print("number is not palindrome")  

# print("============================(binary colde)===================================")
# import math
# b=" "
# n=int(input("enter any number"))
# while(n!=0):
#      rem=n%2
#      b=str(rem)+b
#      n=math.floor(n/2)
# print(b,end=" ")

print("============================(bite code repace)===================================")


# import math
# b=" "
# x=" "
# n=int(input("enter any number"))
# while(n!=0):
#      rem=n%2
#      b=str(rem)+b
#      if rem==0:
#       x="1"+ x
#      else:
#        x="0"+ x 
#      n=math.floor(n/2)
# print(x)
# print(b)
# print("=========================(binary to desimal )===============================")


import math
n=int(input("enter binary code"))
sum=0
p=0
while(n!=0):
    rem=(n%10)
    sum=sum+rem*math.pow(2,p)
    p+=1
    n=math.floor(n/10)
print(int(sum))





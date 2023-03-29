# # print 
# # 1 2 3  
# # 4 5 6  
# # 7 8 9 pattern
# k=1
# for i in range(1,4):
#     for j in range(1,4):
#         print(k,end=" ")
#         k+=1
#     print(" ")   

# print("------------------------------------------------------------------------------")
# #  print this pattern
# # 9 8 7
# # 6 5 4
# # 3 2 1
# x=9
# for i in range(1,4):
#     for j in range(1,4):
#         print(x,end=" ")
#         x-=1
#     print(" ")     


# print("---------------------------------------------------------------------------")
# # print this pattern
# # 1 
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
# x=int(input("enter any number:"))
# for i in range(1,x):
#     for j in range(1,(i+1)):
#         print(j,end=" ")
#     print(" ")    

# print("-----------------------xoxoxoxoxox---------------------------------------------")
# a=int(input("enter any number"))
# for i in range(a, 0,-1):
#     for j in range(1,(i+1)):
#         print(j,end=" ")
#     print(" ")    


# print("-------------------------------------------------------------------------------")

# #print pattern
# # 1
# # 22
# # 333
# # 4444
# # 55555
# c=int(input("enter any one number"))
# for i in range(1,c):
#     for j in range(1,(i+1)):
#         print(i,end="")
#     print(" ")

# print("================================1=================================")

# # print pattern 
# # 54321
# # 5432
# # 543
# # 54
# # 5

# a=int(input("enter any number:"))
# for i in range(1,a):
#     for j in range(a,(i-1),-1):
#         print(j,end=" ")
#     print(" ") 

# print("======================================================")
# #      * 
# #     ** 
# #    ***
# #   ****
# #  *****
# x=int(input("enter one number:"))
# for i in range(1,x):
#     for j in range(x,(i-1),-1):
#         print(end=" ")
#     for j in range(1,(i+1)):    
#         print("*",end=" ")
#     print(" ")

# print("===========================================")
#         #        1  
#         #       1 2
#         #      1 2 3
#         #     1 2 3 4
#         #    1 2 3 4 5
#         #   1 2 3 4 5 6
#         #  1 2 3 4 5 6 7
#         # 1 2 3 4 5 6 7 8

# b=int(input("enter any nuber"))
# for i in range(1,b+1):
#     for j in range(b,(i-1),-1):
#         print(end=" ")
#     for j in range(1,(i+1)):    
#         print(j,end=" ")
#     print(" ")

# print("===========================================")

#         #      *       
#         #     * *      
#         #    * * *     
#         #   * * * *    
#         #  * * * * *   
#         # * * * * * *  
# a=int(input("enter one number"))
# for i in range(1,a):
#     for j in range(a,(i-1),-1):
#         print(end=" ")
#     for j in range(1,(i+1)):    
#         print("*",end=" ")
#     print(" ")

print("====================not proper output=======================")

    #         
    
x=int (input("enter one number"))
for i in range(1,x):
    for j in range(x,(i-1),-1):
        print(end=" ")
    for j in range(1,(i+1)):
        print(j,end="")
    print(" ")   

print("===========================================")

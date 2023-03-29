# class Xyz:
#     def Add(self,a,b):
#         c=a+b
#         print(c)

# class Abc(Xyz):
#     def Sub(self,a,b):
#         c=a-b
#         print(c)


#########################################################################################################  
# a1=Abc()
# a1.Add(10,12)
# class Xyz:
#     def Add(self,a,b):
#         c=a+b
#         print(c)

# class Abc(Xyz):
#     def Add(self,a,b):
#         c=a-b
#         print(c)

# a1=Abc()
# a1.Add(10,12)




class Myclass:
    def Addition(self):
        print("NO PARAMETER")
    def Addition(self,a):
        print("ONE PARAMETER")
    def Addition(self,a,b):
        print("TWO PARAMETER")
    def Addition(self,a,b,c):
        print("THREE PARAMETER")  

m1=Myclass
m1.Addition()
m1.Addition(0)
m1.Addition(1,2)
m1.Addition(1,1,1)







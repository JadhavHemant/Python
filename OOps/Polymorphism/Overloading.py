# class MyClass:
#     def Addition(self):
#         print("Called Default Add Function")
#     def Addition(self,a):
#         print("Called  Add Function with int parameter")
#     def Addition(self,a,b):
#         print("Called  Add Function with two parameters")
#     # def Addition(self,a,b,c):
#     #     print("Called  Add Function with three parameter")

    
# m=MyClass()
# m.Addition(90,89)
# m.Addition(90)
# m.Addition(90,89)
# m.Addition()


class Abc:
    def Add(self,a,b):
        c=a+b
        print("Add=",c)

class Xyz(Abc):
    def Sub(self,a,b):
        c=a-b
        print("Sub=",c)
        
x1=Xyz()
# x1.Sub(90,56)
x1.Add(90,78)
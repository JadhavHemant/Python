# class student:
#     rno=0
#     name=" "
#     def setdata(self,r,n):
#         self.rno=r
#         self.name=n
#     def getdata(self):
#         print(self.rno)
#         print(self.name)
# s=student()

# s.setdata(100,"hemant")            
# s.getdata()


class Myclass:
    a=0
    b=0
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add(self):
        c=self.x+self.y
        print(c)
c1=Myclass(10,20)
c1.add()            



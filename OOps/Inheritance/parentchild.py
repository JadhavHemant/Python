class parent :
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
        print("calling parent class")

    def Add(self):
        c=self.a+self.b
        print("Addition is = ",c)

class child(parent):
    p=0
    b=0
    def __init__(self,l,m):
        self.p=l
        self.q=m
        super().__init__(l,m)
        print("Calling child")

    def Sub(self):
        c=self.p-self.b
        print("Substraction =",c)



c1=child(100,10)
c1.Add()
c1.Sub()

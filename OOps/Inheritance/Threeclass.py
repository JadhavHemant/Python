class parent:
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

class Schild(child):
    h=0
    j=0
    def __init__(self, t, u):
        self.j=t
        self.u=u
        super().__init__(t, u)
        print("Calling Small Child")

    def Mul(self):
        c=self.j*self.u
        print("Mul is = ",c)


c1=Schild(200,10)
c1.Add()
c1.Sub()
c1.Mul()



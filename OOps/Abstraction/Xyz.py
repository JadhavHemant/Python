from abc import ABC
class MyName(ABC):
    def __init__(self) -> None:
        super().__init__()
    def Mul(self):
        pass
    def Div(self):
        pass

class NameMy(MyName):
    def Mul(self):
        print()
    def Div(self):
        print("div")    

x=NameMy()
x.Div()
x.Mul()    





from abc import ABC

class EFG(ABC):
    def __init__(self) -> None:
        super().__init__()
    def Add(self):
        pass
    def Sub(self):
        pass
class Xyz(ABC):
     def Add(self):
        print(" : calling Add function :")
     def Sub(self):
        print(" : calling sub function :")        

a=Xyz()
a.Add()
a.Sub()


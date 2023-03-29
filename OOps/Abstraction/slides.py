from abc import ABC
class MySlide(ABC):
    def __init__(self) -> None:
        super().__init__()
    def trangle(self):
        pass
    def square(self):
        pass 
    def pantagon(self):
        pass
   
class Child(MySlide):

    def trangle(self):
        print("trangle having 3 sides ") 
    def square(self):
        print("square having 4 sides")
    def pantagon(self):
        print("pantagon having 5 sides")
  

c=Child() 
c.trangle()
c.square()
c.pantagon()
class BcsStudent:
    def Details(self):
        print("Calling BCS Studednt Details")
    def Class(self):
        print("Calling Bcs Classs")

class BcaStudent:
    def Details(self):
        print("Calling BCA Studednt Details")
    def Class(self):
        print("Calling BCA Classs")
        
def call(x):
    x.Details()
    x.Class()

bcs=BcsStudent()
bca=BcaStudent()
call(bcs)
call(bca)

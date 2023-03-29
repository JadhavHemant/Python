class BEStudent:
    def Details(self):
        print("BE Student Details are called")
    def Profile(self):
        print("BE Student Profile is called")

class BCAStduent:
    def Details(self):
        print("BCA Student Details are called")
    def Profile(self):
        print("BCA Student Profile is called")


def Call(obj):
    obj.Details()
    obj.Profile()


be=BEStudent()
bca=BCAStduent()
Call(be)
Call(bca)

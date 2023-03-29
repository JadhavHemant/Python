class Products:
    Product=[]
    

    def AddProduct(self):
        productId=int(input("Enter Product Id : "))
        ProductName=input("Enter Product Name : ")
        productPrice=input("Enter product price")
        productRating=int(input("Enter Product Ratting"))
        productStock=int(input("Enter product stock"))


        prod={"productId":productId,"ProductName":ProductName,
        "productPrice":productPrice,"productrating":productRating,
        "productstock":productStock}
        self.Product.append(prod)


    def Displays(self):
        for p in self.Product:
            print(str(p["productId"])+" "+str(p["ProductName"])+
            " "+str(p["productPrice"])+" "+str(p["productrating"])+" "+str(p["productstock"]))


    def SearchByProductName(self):
        x=input("Enter Product Name")
        for a in self.Product:
            if a["ProductName"]==x:
                print(str(a["productId"])+" "+str(a["ProductName"])+
                " "+str(a["productPrice"])+" "+str(a["productrating"])+" "+str(a["productstock"]))





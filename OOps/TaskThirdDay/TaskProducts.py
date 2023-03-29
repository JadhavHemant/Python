from TaskCallProduct import Products
pr=Products()

a=1
while(a!=0):
    x=int(input("Enter Choice : \n1.Add PRoducts : \n2.Display Products : \n3.Search Product By Name : "))
    if(x==1):
        pr.AddProduct()
    elif(x==2):
        pr.Displays()
    elif(x==3):
        pr.SearchByProductName()
    else:
        print("Enter Valid Choice")        

    i=int(input("Do You Wants Add More?yes(1)/no(0): "))       